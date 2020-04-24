import utils as helper


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
