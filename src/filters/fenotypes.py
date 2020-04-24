from filters.frequency import matches_criteria


def dtr(df):
    result = matches_criteria(df, ['ptz', 'atm', 'ctx', 'cro', 'caz', 'fep', 'imp', 'mem', 'ert', 'cip', 'lvx', 'mox'],
                              excluded=['acinetobacter baumannii complex'])
    acineto_result = matches_criteria(df, ['ptz', 'atm', 'ctx', 'cro', 'caz', 'fep', 'imp', 'mem', 'ert', 'cip', 'lvx',
                                           'mox', 'sam'],
                                      included=['acinetobacter baumannii complex'])

    if 'acinetobacter baumannii complex' in acineto_result:
        result['acinetobacter baumannii complex'] = acineto_result.get('acinetobacter baumannii complex')

    return result


