import unittest
from parameterized import parameterized
from filters import frequency
from utils import helper
import pandas as pd
from filters import fenotypes

def initialize_df(resistencia_csv):
    df = pd.read_csv(resistencia_csv, delimiter=';')
    df = helper.normalize_df_headers(df)
    return helper.normalize_resistance_values(df)


class TestFrequency(unittest.TestCase):
    @parameterized.expand([
        ["some_matches", '../test_res/frequency_test/resistencia.csv', 0]
    ])
    @unittest.skip
    def test_multiple_antibiotics(self, name, resistencia_csv, expected):
        df = initialize_df(resistencia_csv)
        result = frequency.matches_criteria(df, ['cip', 'caz'])
        helper.to_csv(result)
        print(result)

        self.assertEqual(0, expected)

    @parameterized.expand([
        ["some_matches", '../test_res/dtr_fenotype/resistencia.csv', 2]
    ])
    @unittest.skip
    def test_dtr(self, name, resistencia_csv, expected):
        df = initialize_df(resistencia_csv)
        result = fenotypes.dtr(df)
        helper.to_csv(result)
        print(result)

        self.assertEqual(result['pseudomonas aeruginosa'].frequency, expected)
        self.assertEqual(result['acinetobacter baumannii complex'].frequency, expected)

    @parameterized.expand([
        ["some_matches", '../test_res/dtr_fenotype/resistencia.csv', 2]
    ])
    def test_cr(self, name, resistencia_csv, expected):
        df = initialize_df(resistencia_csv)
        result = fenotypes.dtr(df)
        helper.to_csv(result)
        print(result)

        self.assertEqual(result['pseudomonas aeruginosa'].frequency, expected)
        self.assertEqual(result['acinetobacter baumannii complex'].frequency, expected)


if __name__ == '__main__':
    unittest.main()
