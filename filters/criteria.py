import pandas as pd
from tqdm import tqdm


def first_criteria(df):
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
    ingresos_last_antibiograms = dict()

    for index, row in df.iterrows():
        if row['nringreso'] not in ingresos_last_antibiograms:
            ingresos_last_antibiograms[row['nringreso']] = dict()

        microorganisms_to_antibiograms = ingresos_last_antibiograms[row['nringreso']]
        if row['microorganismo'] not in microorganisms_to_antibiograms:
            microorganisms_to_antibiograms[row['microorganismo']] = get_antibiogram_signature(row, df)
            continue

        last_antibiogram = microorganisms_to_antibiograms[row['microorganismo']]
        current_antibiogram = get_antibiogram_signature(row, df)
        if last_antibiogram != current_antibiogram:
            microorganisms_to_antibiograms[row['microorganismo']] = current_antibiogram
            continue

        df.drop(index, inplace=True)
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