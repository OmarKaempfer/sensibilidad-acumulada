from filters.frequency import matches_criteria
from utils.helper import *

watched_microorganisms = ['enterobacter', 'escherichia coli', 'klebsiella', 'pseudomonas aeruginosa',
                          'acinetobacter baumannii', 'acinetobacter nosocomialis', 'acinetobacter pittii',
                          'acinetobacter dijkshoorniae', 'acinetobacter seifertii']
dtr_antibiotics = ['ptz', 'atm', 'ctx', 'cro', 'caz', 'fep', 'imp', 'mem', 'ert', 'cip', 'lvx', 'mox']
acinetobacter_baumannii_complex = ['acinetobacter baumannii', 'acinetobacter nosocomialis', 'acinetobacter pittii', 'acinetobacter dijkshoorniae', 'acinetobacter seifertii']
acinetobacter_baumannii_complex_dtr_antibiotics = ['ptz', 'atm', 'ctx', 'cro', 'caz', 'fep', 'imp', 'mem', 'ert', 'cip', 'lvx', 'mox', 'sam']

enterobacter_cr_antibiotics = ['ert', 'imp', 'mem']
pseudomonas_aeruginosa_cr_antibiotics = ['imp', 'mem']

enterobacter_ecr_antibiotics = ['ctx', 'cro', 'caz', 'fep']
pseudomonas_aeruginosa_ecr_antibiotics = ['caz', 'fep']

enterobacter_fqr_antibiotics = ['cip', 'lvx', 'mox']
pseudomonas_aeruginosa_fqr_antibiotics = ['cip', 'lvx']


def dtr(df):
    result = matches_criteria(df, dtr_antibiotics,
                              excluded=acinetobacter_baumannii_complex)
    acineto_result = matches_criteria(df, acinetobacter_baumannii_complex_dtr_antibiotics,
                                      included=acinetobacter_baumannii_complex)

    if 'acinetobacter baumannii complex' in acineto_result:
        result['acinetobacter baumannii complex'] = acineto_result.get('acinetobacter baumannii complex')

    return result


def ecr(df):
    result = matches_criteria(df, ['ctx', 'cro', 'caz', 'fep'],
                              included=['enterobacter', 'klebsiella', 'escherichia coli'])
    result.update(matches_criteria(df, ['ctx', 'cro', 'caz', 'fep'],
                                   included=[
                                       'acinetobacter baumannii', 'acinetobacter nosocomialis', 'acinetobacter pittii', 'acinetobacter dijkshoorniae', 'acinetobacter seifertii']))
    result.update(matches_criteria(df, ['caz', 'fep'],
                                   included=['pseudomonas aeruginosa']))

    return result


def is_dtr(row):
    microorganismo_name = get(row, "microorganismo")
    if get_key_matches(acinetobacter_baumannii_complex, microorganismo_name):
        return is_resistant_to_all(row, acinetobacter_baumannii_complex_dtr_antibiotics)
    if get_key_matches(watched_microorganisms, microorganismo_name):
        return is_resistant_to_all(row, dtr_antibiotics)


def is_cr(row):
    microorganismo_name = get(row, "microorganismo")
    if get_key_matches(acinetobacter_baumannii_complex + ['pseudomonas aeruginosa'], microorganismo_name):
        return is_resistant_to_all(row, pseudomonas_aeruginosa_cr_antibiotics)
    if get_key_matches(watched_microorganisms, microorganismo_name):
        return is_resistant_to_all(row, enterobacter_cr_antibiotics)


def is_ecr(row):
    microorganismo_name = get(row, "microorganismo")
    if get_key_matches(['pseudomonas aeruginosa'], microorganismo_name):
        return is_resistant_to_all(row, pseudomonas_aeruginosa_ecr_antibiotics)
    if get_key_matches(watched_microorganisms, microorganismo_name):
        return is_resistant_to_all(row, enterobacter_ecr_antibiotics)


def is_fqr(row):
    microorganismo_name = get(row, "microorganismo")
    if get_key_matches(['pseudomonas aeruginosa'], microorganismo_name):
        return is_resistant_to_all(row, pseudomonas_aeruginosa_fqr_antibiotics)
    if get_key_matches(watched_microorganisms, microorganismo_name):
        return is_resistant_to_all(row, enterobacter_fqr_antibiotics)