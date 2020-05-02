from enum import Enum
from filters import filters


class ReportConfiguration:
    filter_conditions = dict()
    criteria = None
    filters = {'Edad': [], 'Sexo': [], 'Servicio': [], 'Centro': []}
    built_filters = dict()

    def add_filter_condition(self, filter_name, filter_function):
        self.filter_conditions[filter_name] = filter_function

    def remove_filter_condition(self, filter_name):
        self.filter_conditions.pop(filter_name, None)

    def set_criteria(self, criteria):
        self.criteria = criteria

    def get_filter_conditions(self):
        return self.filter_conditions

    def clear_filters(self):
        self.filters = {'Edad': [], 'Sexo': [], 'Servicio': [], 'Centro': []}

    def build_filters(self):
        self.clear_filters()
        for filter_condition in self.filter_conditions:
            if 'Edad' in filter_condition:
                self.filters['Edad'] += [self.filter_conditions[filter_condition]]
            if 'Servicio' in filter_condition:
                self.filters['Servicio'] += [self.filter_conditions[filter_condition]]
            if 'Centro' in filter_condition:
                self.filters['Centro'] += [self.filter_conditions[filter_condition]]
            if 'Sexo' in filter_condition:
                self.filters['Sexo'] += [self.filter_conditions[filter_condition]]

        self.built_filters['Edad'] = lambda df: filters.age(df, *self.filters['Edad'])
        self.built_filters['Servicio'] = lambda df: filters.service_area(df, *self.filters['Servicio'])
        self.built_filters['Centro'] = lambda df: filters.center(df, *self.filters['Centro'])
        self.built_filters['Sexo'] = lambda df: filters.gender(df, *self.filters['Sexo'])

        return self.built_filters


class Criteria(Enum):
    FIRST_CRITERIA = 1
    SECOND_CRITERIA = 2
    FOURTH_CRITERIA = 4

    def get_description(self):
        if self is self.FIRST_CRITERIA:
            return "Primer microorganismo por paciente independientemente de su sensibilidad o tipo"
