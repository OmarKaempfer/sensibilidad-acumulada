from enum import Enum


class ReportConfiguration:
    filters = dict()
    criteria = None

    def add_filter(self, filter_name, filter_function):
        self.filters[filter_name] = filter_function

    def remove_filter(self, filter_name):
        self.filters.pop(filter_name, None)

    def set_criteria(self, criteria):
        self.criteria = criteria

    def get_filters(self):
        return self.filters


class Criteria(Enum):
    FIRST_CRITERIA = 1
    SECOND_CRITERIA = 2
    FOURTH_CRITERIA = 4

    def get_description(self):
        if self is self.FIRST_CRITERIA:
            return "Primer microorganismo por paciente independientemente de su sensibilidad o tipo"
