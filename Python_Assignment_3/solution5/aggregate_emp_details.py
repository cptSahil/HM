"""
    Importing all the required libraries to run the program.
"""
import json
from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time #pylint: disable=import-error disable=wrong-import-position

@log_execution_time
def aggregate_employee_data():
    """
        Aggregate employee data by Business Unit and store in a new JSON file.

        Return:
        None
    """

    # Load data from the existing JSON file
    with open('..solution4/Employee_Personal_Details.json', 'r',encoding='utf-8') as file:
        emp_data = json.load(file)

    business_units = {}
    for employee in emp_data:
        unit = employee['Business Unit']
        if unit not in business_units:
            business_units[unit] = []
        business_units[unit].append(employee)

    with open('Aggregated_emp_data.json', 'w', encoding='utf-8') as file:
        json.dump(business_units, file, indent = 4)

if __name__ == "__main__":
    aggregate_employee_data()
