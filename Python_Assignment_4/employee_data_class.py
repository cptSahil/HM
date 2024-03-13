"""importing the necessary module required"""
import json
from faker import Faker
from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time

fake = Faker()

class Employee:
    """Class to represent an employee."""
    def __init__(self,emp_id=None, emp_name=None, emp_email=None, business_unit=None, salary=None): #pylint: disable=too-many-arguments
        """Initialize an Employee object with provided or default values."""
        self.set_emp_id(emp_id)
        self.set_emp_name(emp_name)
        self.set_emp_email(emp_email)
        self.set_business_unit(business_unit)
        self.set_salary(salary)

    def set_emp_id(self, emp_id=None):
        """Set the employee ID."""
        self.emp_id = emp_id if emp_id is not None else fake.random_int(1000, 9999)

    def set_emp_name(self, emp_name=None):
        """Set the employee name."""
        self.emp_name = emp_name if emp_name is not None else fake.name()

    def set_emp_email(self, emp_email=None):
        """Set the employee email."""
        self.emp_email = emp_email if emp_email is not None else fake.email()

    def set_business_unit(self, business_unit=None):
        """Set the employee business unit."""
        self.business_unit = business_unit if business_unit is not None else fake.company()

    def set_salary(self, salary=None):
        """Set the employee salary."""
        self.salary = salary if salary is not None else fake.random_int(30000, 100000)

    def get_emp_id(self):
        """Get the employee ID."""
        return self.emp_id

    def get_emp_name(self):
        """Get the employee name."""
        return self.emp_name

    def get_emp_email(self):
        """Get the employee email."""
        return self.emp_email

    def get_business_unit(self):
        """Get the employee business unit."""
        return self.business_unit

    def get_salary(self):
        """Get the employee salary."""
        return self.salary

    def load_data_to_json(self):
        """Convert the Employee object to a JSON object."""
        return {
            "EMP ID": self.emp_id,
            "EMP NAME": self.emp_name,
            "EMP EMAIL": self.emp_email,
            "Business Unit": self.business_unit,
            "Salary": self.salary
        }

    @classmethod
    def load_employee_data(cls,file_path):
        """Load employee data from a JSON file."""
        with open(file_path, "r",encoding='utf-8') as file:
            employee_data = json.load(file)
        employees = []
        for data in employee_data:
            emp_id = data.get("EMP ID")
            emp_name = data.get("EMP NAME")
            emp_email = data.get("EMP EMAIL")
            business_unit = data.get("Business Unit")
            salary = data.get("Salary")
            employee = Employee(emp_id, emp_name, emp_email, business_unit, salary)
            employees.append(employee)
        return employees

    @staticmethod
    @log_execution_time
    def write_employee_to_file(employee, file_name):
        """Write data for one employee to a JSON file."""
        with open(file_name, "w", encoding='utf-8') as file:
            json.dump(employee.load_data_to_json(), file, indent=4)

    @staticmethod
    @log_execution_time
    def write_employees_to_file(employees, file_name="employees.json"):
        """Write data for a list of employees to a JSON file."""
        data = [emp.load_data_to_json() for emp in employees]
        with open(file_name, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4)

FILEPATH = "C:\\Users\\sahil.yadav\\HM\\Python_Assignment_3\\Employee_Personal_Details.json"
EMPLOYEES = Employee.load_employee_data(FILEPATH)

Employee.write_employee_to_file(EMPLOYEES[0], "one_employee.json")

Employee.write_employees_to_file(EMPLOYEES[:5], "list_of_employees.json")

Employee.write_employees_to_file(EMPLOYEES, "all_employees.json")
