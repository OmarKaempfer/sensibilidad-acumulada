from utils import helper
from filters.fenotypes import *
from model.microorganismo import Microorganismo
from enum import Enum
import pandas as pd


def first_criteria(df):
    """
    First patient microorganism, no sensibility or type criteria considered
    :param df:
    :return:
    """
    ingreso_microorganisms = dict()

    for index, row in df.iterrows():
        if row['nringreso'] not in ingreso_microorganisms:
            ingreso_microorganisms[row['nringreso']] = list()

        microorganisms = ingreso_microorganisms[row['nringreso']]
        if row['microorganismo'] not in microorganisms:
            microorganisms.append(row['microorganismo'])
            ingreso_microorganisms['nringreso'] = microorganisms
            continue

        df.drop(index, inplace=True)

    return df


def second_criteria(df):
    """
    First patient microorganism with a different antibiogram, no type criteria considered
    :param df:
    :return:
    """
    ingresos_last_antibiograms = dict()

    for index, row in df.iterrows():
        if row['nringreso'] not in ingresos_last_antibiograms:
            ingresos_last_antibiograms[row['nringreso']] = dict()

        microorganisms_to_antibiograms = ingresos_last_antibiograms[row['nringreso']]
        if row['microorganismo'] not in microorganisms_to_antibiograms:
            microorganisms_to_antibiograms[row['microorganismo']] = helper.get_antibiogram_signature(row, df)
            continue

        last_antibiogram = microorganisms_to_antibiograms[row['microorganismo']]
        current_antibiogram = helper.get_antibiogram_signature(row, df)
        if last_antibiogram != current_antibiogram:
            microorganisms_to_antibiograms[row['microorganismo']] = current_antibiogram
            continue

        df.drop(index, inplace=True)
    return df


def third_criteria(df):
    """
    The most resistant microorganism of each microorganism
    :param df:
    :return:
    """
    nringreso_strongest_microorganism_resistances = dict()

    for index, row in df.iterrows():
        if row['nringreso'] not in nringreso_strongest_microorganism_resistances:
            nringreso_strongest_microorganism_resistances[row['nringreso']] = dict()

        microorganisms_to_strongest_resistance = nringreso_strongest_microorganism_resistances[row['nringreso']]
        if row['microorganismo'] not in microorganisms_to_strongest_resistance:
            microorganisms_to_strongest_resistance[row['microorganismo']] = (
                helper.get_resistance_value(row, df), index)
            continue

        current_strongest_resistance = microorganisms_to_strongest_resistance[row['microorganismo']]
        current_resistance = (helper.get_resistance_value(row, df), index)
        if current_strongest_resistance[0] < current_resistance[0]:
            df.drop(current_strongest_resistance[1], inplace=True)
            microorganisms_to_strongest_resistance[row['microorganismo']] = (current_resistance, index)
            continue
        else:
            df.drop(index, inplace=True)
    return df


def fourth_criteria(df):
    """
    DTR > CR > ECR > FQR
    :param df:
    :return:
    """
    microorganisms = dict()
    for index, row in df.iterrows():
        microorganism = Microorganismo()
        microorganism.last_register = helper.get(row, 'fechapeticion')
        microorganism.last_nhc = helper.get(row, 'nhc')

        if is_dtr(row):
            microorganism.last_fenotype = ('dtr', 3)
            microorganism.dtr_frequency += 1
        elif is_cr(row):
            microorganism.last_fenotype = ('cr', 2)
            microorganism.cr_frequency += 1
        elif is_ecr(row):
            microorganism.last_fenotype = ('ecr', 1)
            microorganism.ecr_frequency += 1
        elif is_fqr(row):
            microorganism.last_fenotype = ('fqr', 0)
            microorganism.fqr_frequency += 1
        else:
            microorganism.last_fenotype = ('none', -1)

        if helper.get(row, 'microorganismo') in microorganisms:
            saved_record = microorganisms.get(helper.get(row, 'microorganismo'))
            current_date = pd.to_datetime(microorganism.last_register, dayfirst=True)
            last_date = pd.to_datetime(saved_record.last_register, dayfirst=True)
            if (current_date - last_date).days < 30 and saved_record.last_nhc == microorganism.last_nhc:
                if microorganism.last_fenotype[1] >= saved_record.last_fenotype[1]:
                    helper.decrement_frequency(saved_record, saved_record.last_fenotype[0])
                    helper.increment_frequency(saved_record, microorganism.last_fenotype[0])
                    saved_record.last_fenotype = microorganism.last_fenotype
            else:
                helper.increment_frequency(saved_record, microorganism.last_fenotype[0])
                saved_record.frequency += 1
                saved_record.last_nhc = microorganism.last_nhc
                saved_record.last_fenotype = microorganism.last_fenotype
            saved_record.last_register = microorganism.last_register
        else:
            microorganism.frequency = 1
            microorganisms[helper.get(row, 'microorganismo')] = microorganism
    return microorganisms


class Criteria(Enum):
    NONE_CRITERIA = 0
    FIRST_CRITERIA = 1
    SECOND_CRITERIA = 2
    THIRD_CRITERIA = 3
    FOURTH_CRITERIA = 4

    def get_description(self):
        if self is self.NONE_CRITERIA:
            return "Se toman los datos en bruto"
        if self is self.FIRST_CRITERIA:
            return "Primer microorganismo por paciente independientemente de su sensibilidad o tipo"
        if self is self.SECOND_CRITERIA:
            return "Primer microorganismo por paciente con distinto antibiograma independientemente de su sensibilidad o tipo"
        if self is self.THIRD_CRITERIA:
            return "Aislado más resistente de entre todos los aislados del mismo microorganismo"
        if self is self.FOURTH_CRITERIA:
            return "Tabla de frecuencia de pertenencia a cuatro fenotipos jerarquizados: DTR > CR > ECR > FQR. " \
                   "Si pasan más de 30 días entre microorganismos se consideran diferentes, si no se aplica la jerarquía."

    def get_criteria_function(self):
        if self is self.NONE_CRITERIA:
            return lambda df: df
        if self is self.FIRST_CRITERIA:
            return first_criteria
        if self is self.SECOND_CRITERIA:
            return second_criteria
        if self is self.THIRD_CRITERIA:
            return third_criteria
        if self is self.FOURTH_CRITERIA:
            return fourth_criteria
