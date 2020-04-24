import pandas as pd
from cucco import Cucco


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
