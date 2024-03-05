"""Importing all the necessary modules and libraries required."""
import json
import random
from faker import Faker
from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time

fake = Faker()

def generate_employee_data(records): #pylint: disable=redefined-outer-name
    """
        Generate fake employee data.

        Parameters:
        records (int): Number of records to generate.

        Returns:
        list: A List of dictionaries representing employee details.
    """
    employees_data = []
    business_unit_names = ["Developer", "Tester","IT", "Finance", "PP", "Operations", "Marketing"]

    for _ in range(records):
        emp_id = fake.uuid4()[:8]
        emp_name = fake.name()
        emp_email = fake.email()
        business_unit = random.choice(business_unit_names)
        salary = round(random.uniform(30000,80000), 2)

        employee = {
            "EMP ID ": emp_id,
            "EMP NAME": emp_name,
            "EMP EMAIL": emp_email,
            "Business Unit": business_unit,
            "Salary": salary
        }
        employees_data.append(employee)
    return employees_data

@log_execution_time
def main_data():
    """
        Generate fake employee data and write it to a JSON file
    """
    # Generate 50 to 100 records of employee data
    records = random.randint(50,100)
    emp_persoanl_details = generate_employee_data(records)

    # Write data in JSON file
    with open("Employee_Personal_Details.json", "w", encoding='utf-8') as outfile:
        json.dump(emp_persoanl_details, outfile, indent=4)

if __name__ == "__main__":
    main_data()
