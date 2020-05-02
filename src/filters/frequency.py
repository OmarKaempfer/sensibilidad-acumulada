from dataclasses import dataclass
from utils.helper import *


def matches_criteria(dataframe, antibiotics, excluded=None, included=None):
    microorganismos = dict()
    for index, row in dataframe.iterrows():
        microorganismo_name = get(row, "microorganismo")
        if (excluded is not None) and get_key_matches(excluded, microorganismo_name):
            continue
        if (included is not None) and not get_key_matches(included, microorganismo_name):
            continue

        if is_resistant_to_all(row, antibiotics):
            if microorganismo_name in microorganismos:
                microorganismo = microorganismos.get(microorganismo_name)
                microorganismo.frequency += 1
            else:
                microorganismo = Microorganism(resistant_to=antibiotics)
                microorganismo.frequency += 1
                microorganismos[microorganismo_name] = microorganismo
    return microorganismos


def get_sensibility_percentages(df):
    microorganisms = dict()
    antibiotics = get_all_antibiotics(df)

    for index, row in df.iterrows():
        if get(row, 'microorganismo') in microorganisms:
            microorganism_record = microorganisms.get(get(row, 'microorganismo'))
        else:
            microorganism_record = initialize_microorganism_record(row, antibiotics)
            microorganisms[get(row, 'microorganismo')] = microorganism_record

        for antibiotic in antibiotics:
            antibiotic_resistance = get(row, antibiotic)
            if antibiotic_resistance != 'nan':
                microorganism_record.sensibility[antibiotic].total += 1
            if antibiotic_resistance == 'sensible' or antibiotic_resistance == 'intermedio':
                microorganism_record.sensibility[antibiotic].sensible += 1
            if microorganism_record.sensibility[antibiotic].total != 0:
                microorganism_record.sensibility[antibiotic].percentage = \
                    microorganism_record.sensibility[antibiotic].sensible / microorganism_record.sensibility[antibiotic].total
        microorganism_record.frequency += 1

    return microorganisms


def initialize_microorganism_record(row, antibiotics):
    microorganism_record = Microorganism(get(row, 'microorganismo'))
    microorganism_sensibility = dict()
    for antibiotic in antibiotics:
        microorganism_sensibility[antibiotic] = SensibilityRecord()
    microorganism_record.sensibility = microorganism_sensibility
    return microorganism_record


@dataclass
class Microorganism:
    name: str
    sensibility: dict = None
    frequency: int = 0


@dataclass
class SensibilityRecord:
    total: int = 0
    sensible: int = 0
    percentage: float = 0
