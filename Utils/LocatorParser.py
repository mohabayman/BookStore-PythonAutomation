import robot.api
import re
from collections import defaultdict


class LocatorParser(object):
    @staticmethod
    def get_Locators(file_name):
        resource_file = robot.api.ResourceFile(source=file_name).populate()
        variables = resource_file.variable_table.variables
        vars_dict = defaultdict(list)
        for var in variables:
            if var.name:
                name = re.sub('[${}]', '', var.name)
                vars_dict[name].append(var.value[0])
                vars_dict[name].append(var.value[1])

        return vars_dict