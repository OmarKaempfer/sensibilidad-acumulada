import pandas as pd
import utils.helper as helper
import filters.criteria as criteria
from cucco import Cucco
import tqdm


def sensibilidad_acumulada(csv_path):
    episodio_duration = 6
    ingreso_duration = 14

    df = pd.read_csv(csv_path, delimiter=';')
    df = helper.normalize_df_headers(df)
    df = helper.normalize_resistance_values(df)
    df = ingreso_episode_ordering(df, episodio_duration, ingreso_duration)
    df = helper.reorder_columns(df)
    df = criteria.third_criteria(df)
    df.to_csv('result/result.csv', encoding='utf-8-sig', sep=';')


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
    sensibilidad_acumulada("test-res/resistencia2.csv")