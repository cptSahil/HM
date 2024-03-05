"""Importing necessary modules"""
import json
from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time

@log_execution_time
def hike(business_units): #pylint: disable=redefined-outer-name
    """
    Update the salary hike of the business units.
    Parameters:
    business_units (dict): A dictionary containing employee data with hiked salary by Business Unit.
    Returns:
    list: An updated list of names of the aggregate employees.
    """
    while True:
        business_unit = input("Enter the business unit (or type 'done' to finish): ")
        if business_unit.lower() == 'done':
            break
        percentage = float(input("Enter the salary hike percentage: "))
        if business_unit in business_units:
            for employee in business_units[business_unit]:
                employee['Salary'] *= (1 + round(percentage / 100,2))
if __name__ == "__main__":
   # Loading aggregated employee data
    with open('Aggregated_emp_data.json', 'r', encoding='utf-8') as file:
        business_units = json.load(file)
    # Updating salary hike for multiple business units
    hike(business_units)
    # Saving updated data to a new JSON file
    with open('Hiked_Salary.json', 'w', encoding='utf-8') as file:
        json.dump(business_units, file, indent=4)
