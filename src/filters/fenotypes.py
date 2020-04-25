from filters.frequency import matches_criteria


def dtr(df):
    result = matches_criteria(df, ['ptz', 'atm', 'ctx', 'cro', 'caz', 'fep', 'imp', 'mem', 'ert', 'cip', 'lvx', 'mox'],
                              excluded=[
                                       'acinetobacter baumannii', 'acinetobacter nosocomialis', 'acinetobacter pittii', 'acinetobacter dijkshoorniae', 'acinetobacter seifertii'])
    acineto_result = matches_criteria(df, ['ptz', 'atm', 'ctx', 'cro', 'caz', 'fep', 'imp', 'mem', 'ert', 'cip', 'lvx',
                                           'mox', 'sam'],
                                      included=['acinetobacter baumannii complex'])

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
