"""
This module contains a class called Employee which represents an employee.
It also has methods to set default values for these attributes using the Faker library.
The class has a method load_employee_data which converts the employee object to a json object.
The class also has a static method write_employee_to_file and write_employees_to_file
which takes an employee object or a list of employee objects and
writes the json representation of the object(s) to a file. It also log the module name and
date time of the function call in the logs folder.
"""
import json
from faker import Faker
from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time

fake = Faker()

class Employee:
    """Class to represent an employee."""
    def __init__(self,emp_id=None, emp_name=None, emp_email=None, business_unit=None, salary=None): #pylint: disable=too-many-arguments
        """_summary_

        Args:
            emp_id (_type_, optional): employee id. Defaults to None.
            emp_name (_type_, optional): employee name. Defaults to None.
            emp_email (_type_, optional): employee email. Defaults to None.
            business_unit (_type_, optional): business unit. Defaults to None.
            salary (_type_, optional): Salary. Defaults to None.
        """
        self.set_emp_id(emp_id)
        self.set_emp_name(emp_name)
        self.set_emp_email(emp_email)
        self.set_business_unit(business_unit)
        self.set_salary(salary)

    #setter methods to set values
    def set_emp_id(self, emp_id=None):
        """Sets the employee's id to the provided value

        Args:
            emp_id (_type_, optional): _description_. Defaults to None.
        """
        self.emp_id = emp_id if emp_id is not None else fake.random_int(1000, 9999)

    def set_emp_name(self, emp_name=None):
        """Sets the employee's name to the provided value

        Args:
            emp_name (_type_, optional): _description_. Defaults to None.
        """
        self.emp_name = emp_name if emp_name is not None else fake.name()

    def set_emp_email(self, emp_email=None):
        """Sets the employee's email to the provided value.

        Args:
            emp_email (_type_, optional): _description_. Defaults to None.
        """
        self.emp_email = emp_email if emp_email is not None else fake.email()

    def set_business_unit(self, business_unit=None):
        """Sets the business unit to the provided value.

        Args:
            business_unit (_type_, optional): _description_. Defaults to None.
        """
        self.business_unit = business_unit if business_unit is not None else fake.company()

    def set_salary(self, salary=None):
        """Sets the employee's salary to the provided value.

        Args:
            salary (_type_, optional): _description_. Defaults to None.
        """
        self.salary = salary if salary is not None else fake.random_int(30000, 100000)

    #getter methods to get the values
    def get_emp_id(self):
        """Gets the employee ID for this Employee object.

        Returns:
            emp_id - int: the employee's ID number
        """
        return self.emp_id

    def get_emp_name(self):
        """Gets the employee name for this Employee object.

        Returns:
            emp_name - str: the employee's name.
        """
        return self.emp_name

    def get_emp_email(self):
        """Gets the employee email for this Employee object.

        Returns:
            emp_email - str: the employee's email address.
        """
        return self.emp_email

    def get_business_unit(self):
        """Gets the business unit for this Employee object.

        Returns:
            business_unit - str: The employee's business unit.
        """
        return self.business_unit

    def get_salary(self):
        """Gets the employee's salary for this Employee object.

        Returns:
            salary - float: The employee's salary.
        """
        return self.salary

    def load_data_to_json(self):
        """Convert the Employee object to a JSON object.
        
        Args:
            None

        Returns:
            {} - dict: A dictionary containing employee ID, name, email, business unit, and salary.
        """
        return {
            "EMP ID": self.emp_id,
            "EMP NAME": self.emp_name,
            "EMP EMAIL": self.emp_email,
            "Business Unit": self.business_unit,
            "Salary": self.salary
        }

    @classmethod
    def load_employee_data(cls,file_path):
        """class method that helps to load the data of employee

        Args:
            file_path : get the data from the json file store in the directory.

        Returns:
            employee - dict: return employee data
        """
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
        """Static method that converts employee data to JSON format and writes it to a file.

        Args:
            employee : Employee object of employee objects to  be converted
            file_name (str):  File name in which to write the JSON data.

        Returns:
            None
        """
        with open(file_name, "w", encoding='utf-8') as file:
            json.dump(employee.load_data_to_json(), file, indent=4)

    @staticmethod
    @log_execution_time
    def write_employees_to_file(employees, file_name="employees.json"):
        """Static method that converts employee data to JSON format and writes it to a file.

        Args:
            employees : Employee object or list of employee objects to  be converted
            file_name (str):  File name in which to write the JSON data.

        Returns:
            None
        """
        data = [emp.load_data_to_json() for emp in employees]
        with open(file_name, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4)

FILEPATH = "C:\\Users\\sahil.yadav\\HM\\Python_Assignment_3\\Employee_Personal_Details.json"
EMPLOYEES = Employee.load_employee_data(FILEPATH)

Employee.write_employee_to_file(EMPLOYEES[0], "one_employee.json")

Employee.write_employees_to_file(EMPLOYEES[:5], "list_of_employees.json")

Employee.write_employees_to_file(EMPLOYEES, "all_employees.json")
