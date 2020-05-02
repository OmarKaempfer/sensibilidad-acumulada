from utils.helper import *


def culture_type(df, *types):
    return filter_by_column_value(df, 'tipodemuestra', *types)


def service_area(df, *service_areas):
    return filter_by_column_value(df, 'servicio', *service_areas)


def gender(df, *genders):
    return filter_by_column_value(df, 'sexo', *genders)


def center(df, *centers):
    return filter_by_column_value(df, 'centro', *centers)


def filter_by_column_value(df, column, *column_values):
    if not column_values:
        return df
    for index, row in df.iterrows():
        complies_with_any = False
        for current_type in column_values:
            print(get(row, column))
            if get(row, column) == str.lower(current_type):
                complies_with_any = True
        if not complies_with_any:
            df.drop(index, inplace=True)
    return df


def age(df, *age_conditions):
    if not age_conditions:
        return df
    for index, row in df.iterrows():
        for age_condition in age_conditions:
            if not age_condition(get_age(row)):
                df.drop(index, inplace=True)

    return df


def age_higher_than(threshold_age):
    return lambda a: a > float(threshold_age)


def age_lower_than(threshold_age):
    return lambda a: a < float(threshold_age)

