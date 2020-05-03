import pandas as pd
from cucco import Cucco
from filters import filters
from filters.criteria import Criteria


def normalize_df_headers(df):
    norm_esp = Cucco()

    headers = df.columns
    normalized_headers = []
    for header in headers:
        normalized_header = norm_esp.normalize(str.lower(header).replace(' ', '')).replace('–', '_')
        normalized_headers.append(
            normalized_header if len(normalized_header) != 0 else str.lower(header))

    df.columns = normalized_headers
    return df


def normalize_resistance_values(df):
    df = df.replace(to_replace="0.0", value="resistente") \
        .replace(to_replace="-0", value="sensible") \
        .replace(to_replace="+0", value="resistente") \
        .replace(to_replace="0", value="resistente") \
        .replace(to_replace="+", value="resistente") \
        .replace(to_replace="-", value="sensible")
    return df


def reorder_columns(df):
    first_cols = ['nringreso', 'nrepisodio', 'peticion', 'fechapeticion', 'nhc', 'microorganismo', 'paciente']
    last_cols = [col for col in df.columns if col not in first_cols]
    df = df[first_cols + last_cols]
    return df


def get_antibiogram_signature(row, df):
    start_antibiogram_index = df.columns.get_loc('numeroaislamiento') + 1
    antibiogram_signature = ""
    for i in range(start_antibiogram_index, len(df.columns), 2):
        if pd.isnull(row[i]):
            antibiogram_signature += '0'
        if row[i] == 'Resistente':
            antibiogram_signature += '1'
        if row[i] == 'Sensible':
            antibiogram_signature += '2'
        if row[i] == 'Intermedio':
            antibiogram_signature += '3'

    return antibiogram_signature


def get_resistance_value(row, df):
    start_antibiogram_index = df.columns.get_loc('numeroaislamiento') + 1
    microorganism_resistance = 0
    antibiotics_tested = 0
    for i in range(start_antibiogram_index, len(df.columns), 2):
        if pd.isnull(row[i]):
            continue
        if row[i] == 'Resistente':
            microorganism_resistance += 2
        if row[i] == 'Intermedio':
            microorganism_resistance += 1
        antibiotics_tested += 1

    microorganism_resistance = microorganism_resistance / antibiotics_tested
    return microorganism_resistance


def update_indices(dictionary, removed):
    for key in dictionary:
        for internal_key in dictionary[key]:
            if dictionary[key][internal_key][1] > removed:
                dictionary[key][internal_key] = (dictionary[key][internal_key][0], dictionary[key][internal_key][1] - 1)


def to_csv(dictionary):
    df = pd.DataFrame(columns=["Microorganismo", "Resistentes", "Frecuencia"])
    for key in dictionary:
        microorganismo_record = dictionary[key]
        df = df.append({'Microorganismo': key, 'Resistentes': microorganismo_record.resistant_to, 'Frecuencia': microorganismo_record.frequency}, ignore_index=True)
    df.to_csv('../result/frequency.csv', encoding='utf-8-sig', sep=';', index=False)


def to_csv_fourth_criteria(dictionary, path):
    df = pd.DataFrame(columns=["Microorganismo", "Frecuencia", "Frecuencia DTR",  "Frecuencia CR", "Frecuencia ECR", "Frecuencia FQR"])
    for key in dictionary:
        microorganismo_record = dictionary[key]
        df = df.append({'Microorganismo': key, 'Frecuencia': microorganismo_record.frequency,
                        'Frecuencia DTR': microorganismo_record.dtr_frequency,
                        'Frecuencia CR': microorganismo_record.cr_frequency,
                        'Frecuencia ECR': microorganismo_record.ecr_frequency,
                        'Frecuencia FQR': microorganismo_record.fqr_frequency}, ignore_index=True)
    df.to_csv(path, encoding='utf-8-sig', sep=';', index=False)


def to_csv_sensitivity_records(microorganisms, path):
    sensitivity_df = pd.DataFrame()
    sensitivity_df = sensitivity_df.append(list(map(to_row, microorganisms.values())), ignore_index=True)
    sensitivity_df.to_csv(path, encoding='utf-8-sig', sep=';', index=False)
    return sensitivity_df


def to_row(microorganism):
    row = dict()
    row['Total'] = microorganism.frequency
    row['Microorganismo'] = microorganism.name
    for antibiotic in microorganism.sensibility:
        row[antibiotic] = to_tuple(microorganism.sensibility[antibiotic])

    return row


def to_tuple(sensibility_record): return sensibility_record.sensible, sensibility_record.total, sensibility_record.percentage


def is_resistant_to_all(row, antibiotics):
    for antibiotic in antibiotics:
        resistance = get(row, antibiotic)
        if resistance != 'resistente':
            return False

    return True


def get(row, field_name):
    if field_name in row:
        return str(row[field_name]).lower()
    return None


def get_key_matches(list_variable, name):
    result_list = []
    if list_variable is None:
        return result_list
    for item in list_variable:
        if item in name:
            result_list.append(item)

    return result_list


def decrement_frequency(microorganism, fenotype):
    if fenotype == 'dtr':
        microorganism.dtr_frequency -= 1
    if fenotype == 'cr':
        microorganism.cr_frequency -= 1
    if fenotype == 'ecr':
        microorganism.ecr_frequency -= 1
    if fenotype == 'fqr':
        microorganism.fqr_frequency -= 1


def increment_frequency(microorganism, fenotype):
    if fenotype == 'dtr':
        microorganism.dtr_frequency += 1
    if fenotype == 'cr':
        microorganism.cr_frequency += 1
    if fenotype == 'ecr':
        microorganism.ecr_frequency += 1
    if fenotype == 'fqr':
        microorganism.fqr_frequency += 1


def get_all_antibiotics(df):
    start_antibiogram_index = df.columns.get_loc('numeroaislamiento') + 1
    antibiotics = []
    for i in range(start_antibiogram_index, len(df.columns), 2):
        antibiotics = antibiotics + [df.columns[i]]
    return antibiotics


def get_age(row):
    fecha_peticion = pd.to_datetime(get(row, 'fechapeticion'), dayfirst=True)
    fecha_nacimiento = pd.to_datetime(get(row, 'fechanacimiento'), dayfirst=True)
    return (fecha_peticion - fecha_nacimiento).days / 365.25


def get_age_filter_condition(age_value, operator):
    if operator == '>':
        return filters.age_higher_than(float(age_value))
    else:
        return filters.age_lower_than(float(age_value))


def get_sex_condition(sex_value):
    if sex_value == 'Hombre':
        return 'M'
    else:
        return 'F'


def get_service_condition(service):
    return str.lower(service)


def get_center_condition(center):
    return str.lower(center)


def get_criteria(text):
    if text == 'Ninguno':
        return Criteria.NONE_CRITERIA
    if text == 'Primero':
        return Criteria.FIRST_CRITERIA
    if text == 'Segundo':
        return Criteria.SECOND_CRITERIA
    if text == 'Tercero':
        return Criteria.THIRD_CRITERIA
    if text == 'DTR':
        return Criteria.FOURTH_CRITERIA
