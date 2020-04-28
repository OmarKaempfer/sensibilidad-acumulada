import unittest
from parameterized import parameterized
from filters import frequency
from report_generator import ingreso_episode_ordering
from filters import fenotypes
from filters.criteria import *

episodio_duration = 6
ingreso_duration = 14


def initialize_df(resistencia_csv):
    df = pd.read_csv(resistencia_csv, delimiter=';')
    df = normalize_df_headers(df)
    df = normalize_resistance_values(df)
    df = ingreso_episode_ordering(df, episodio_duration, ingreso_duration)
    return normalize_resistance_values(df)


class TestFrequency(unittest.TestCase):
    @parameterized.expand([
        ["some_matches", '../test_res/frequency_test/resistencia.csv', 0]
    ])
    @unittest.skip
    def test_multiple_antibiotics(self, name, resistencia_csv, expected):
        df = initialize_df(resistencia_csv)
        result = frequency.matches_criteria(df, ['cip', 'caz'])
        to_csv(result)
        print(result)

        self.assertEqual(0, expected)

    @parameterized.expand([
        ["some_matches", '../test_res/dtr_fenotype/resistencia.csv', 2]
    ])
    @unittest.skip
    def test_dtr(self, name, resistencia_csv, expected):
        df = initialize_df(resistencia_csv)
        result = fenotypes.dtr(df)
        to_csv(result)
        print(result)

        self.assertEqual(result['pseudomonas aeruginosa'].frequency, expected)
        self.assertEqual(result['acinetobacter baumannii complex'].frequency, expected)

    @parameterized.expand([
        ["some_matches", '../test_res/ecr_fenotype/resistencia.csv', {'enterobacter test1': 1,
                                                                      'enterobacter test2': 1,
                                                                      'klebsiella pneumoniae': 1,
                                                                      'klebsiella faecallis': 1,
                                                                      'acinetobacter baumannii': 1,
                                                                      'acinetobacter nosocomialis': 1,
                                                                      'acinetobacter pittii': 1,
                                                                      'acinetobacter dijkshoorniae': 1,
                                                                      'acinetobacter seifertii': 1,
                                                                      'escherichia coli': 1,
                                                                      'pseudomonas aeruginosa': 1}]
    ])
    @unittest.skip
    def test_ecr(self, name, resistencia_csv, expected):
        df = initialize_df(resistencia_csv)
        result = fenotypes.ecr(df)
        to_csv(result)
        print(result)
        for key in expected:
            self.assertEqual(result[key].frequency, expected[key], key)

    '''
    Expected
    dtr 2
    fqr 2
    cr 1
    ecr 1
    freq 8


    pseudomonas
    freq 3
    dtr 1
    fqr 
    cr
    ecr 1

    acinetobacter nosocomialis
    freq 2
    dtr 1
    cr 1
    ecr
    fqr
    '''
    @parameterized.expand([
        ["some_matches", '../test_res/fourth_criteria/resistencia.csv']
    ])
    @unittest.skip
    def test_fourth_criteria(self, name, resistencia_csv):
        df = initialize_df(resistencia_csv)
        result = fourth_criteria(df)
        to_csv_fourth_criteria(result)
        print(result)

    @parameterized.expand([
        ["some_matches", '../test_res/fourth_criteria/resistencia.csv']
    ])
    def test_sensibility_percentages(self, name, resistencia_csv):
        df = initialize_df(resistencia_csv)
        df = reorder_columns(df)
        to_csv_sensitivity_records(df, frequency.get_sensibility_percentages(df))


if __name__ == '__main__':
    unittest.main()
