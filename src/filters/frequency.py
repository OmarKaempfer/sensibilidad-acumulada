from model.microorganismo import Microorganismo
from utils.helper import *


def matches_criteria(dataframe, antibiotics, excluded=None, included=None):
    microorganismos = dict()
    for index, row in dataframe.iterrows():
        microorganismo_name = get(row, "microorganismo")
        if (excluded is not None) and get_key_matches(excluded, microorganismo_name):
            continue
        if (included is not None) and not get_key_matches(included, microorganismo_name):
            continue

        if is_resistant_to_all(row, antibiotics):
            if microorganismo_name in microorganismos:
                microorganismo = microorganismos.get(microorganismo_name)
                microorganismo.frequency += 1
            else:
                microorganismo = Microorganismo(resistant_to=antibiotics)
                microorganismo.frequency += 1
                microorganismos[microorganismo_name] = microorganismo
    return microorganismos
