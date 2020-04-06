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