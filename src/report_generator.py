import pandas as pd

from filters.criteria import *
from utils import helper
from filters import frequency


def sensibilidad_acumulada(csv_path, report_configuration):
    episodio_duration = 6
    ingreso_duration = 14
    df = pd.read_csv(report_configuration.initial_csv_path, delimiter=';')
    df = helper.normalize_df_headers(df)
    df = helper.normalize_resistance_values(df)
    df = ingreso_episode_ordering(df, episodio_duration, ingreso_duration)
    df = helper.reorder_columns(df)
    built_filters = report_configuration.build_filters()
    for current_filter in built_filters:
        df = built_filters[current_filter](df)

    df = report_configuration.criteria.get_criteria_function()(df)
    if report_configuration.dtr_fenotype:
        helper.to_csv_fourth_criteria(fourth_criteria(df), report_configuration.dtr_fenotype_path)
    helper.to_csv_sensitivity_records(frequency.get_sensibility_percentages(df), report_configuration.sensitivity_table_path)
    df.to_csv(report_configuration.final_csv_path, encoding='utf-8-sig', sep=';')


def ingreso_episode_ordering(df, episodio_duration, ingreso_duration):
    df['fechapeticion'] = pd.to_datetime(df['fechapeticion'], dayfirst=True)
    df.sort_values(['nhc', 'fechapeticion'], ascending=[True, True], inplace=True)
    df.index = pd.RangeIndex(len(df.index))
    df["nringreso"] = ""
    df["nrepisodio"] = ""
    df = set_ingreso_episodio_index(df, episodio_duration, ingreso_duration)
    return df


def set_ingreso_episodio_index(df, episodio_duration, ingreso_duration):
    nringreso = 1
    nrepisodio = 1

    for index in df.index:
        if index == 0:
            df.loc[index, 'nrepisodio'] = nrepisodio
            df.loc[index, 'nringreso'] = nringreso
            continue
        if df['nhc'][index] == df['nhc'][index - 1]:

            previous_date = df['fechapeticion'][index - 1]
            current_date = df['fechapeticion'][index]

            if (current_date - previous_date).days > episodio_duration:
                nrepisodio += 1
                if (current_date - previous_date).days > ingreso_duration:
                    nrepisodio = 1
                    nringreso += 1
        else:
            nringreso += 1
            nrepisodio = 1

        df.loc[index, 'nrepisodio'] = nrepisodio
        df.loc[index, 'nringreso'] = nringreso

    return df


if __name__ == '__main__':
    sensibilidad_acumulada("../test_res/resistencia2.csv")