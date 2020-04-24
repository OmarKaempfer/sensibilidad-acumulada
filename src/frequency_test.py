import unittest
from parameterized import parameterized
from filters import frequency
from utils import helper
import pandas as pd


class TestFrequency(unittest.TestCase):
    @parameterized.expand([
        ["some_matches", '../test_res/frequency_test/resistencia.csv', 0]
    ])
    def test_multiple_antibiotics(self, name, resistencia_csv, expected):
        df = pd.read_csv(resistencia_csv, delimiter=';')
        df = helper.normalize_df_headers(df)
        df = helper.normalize_resistance_values(df)
        result = frequency.matches_criteria(df, ['cip', 'caz'])
        helper.to_csv(result)
        print(result)

        self.assertEqual(0, expected)


if __name__ == '__main__':
    unittest.main()
