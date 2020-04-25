from model.microorganismo import Microorganismo


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
                microorganismo = Microorganismo(resistant_to=antibiotics)
                microorganismo.frequency += 1
                microorganismos[microorganismo_name] = microorganismo
    return microorganismos


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
