from cucco import Cucco


def normalize_df_headers(df):
    norm_esp = Cucco()

    headers = df.columns
    normalized_headers = []
    for header in headers:
        normalized_header = norm_esp.normalize(str.lower(header).replace(' ', '')).replace('–', '_')
        normalized_headers.append(
            normalized_header if len(normalized_header) != 0 else str.lower(header))

    df.columns = normalized_headers
    return df


def normalize_resistance_values(df):
    df = df.replace(to_replace="0.0", value="resistente")\
                         .replace(to_replace="-0", value="sensible")\
                         .replace(to_replace="+0", value="resistente")\
                         .replace(to_replace="0", value="resistente")\
                         .replace(to_replace="+", value="resistente")\
                         .replace(to_replace="-", value="sensible")
    return df


def reorder_columns(df):
    first_cols = ['nringreso', 'nrepisodio', 'peticion', 'fechapeticion', 'nhc', 'microorganismo','paciente']
    last_cols = [col for col in df.columns if col not in first_cols]
    df = df[first_cols + last_cols]
    return df
