"""
    Importing the the necessary libraries to run the program.
"""
import random
from faker import Faker
import pandas as pd
from tabulate import tabulate
from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time

def create_employee_excel():
    """
    Function to create an Excel file with employee data generated using Faker.
    """
    fake = Faker()
    emp_data = {
        "emp_id": [random.randint(1, 1000) for _ in range(100)],
        "emp_name": [fake.name() for _ in range(100)],
        "emp_email": [fake.email() for _ in range(100)],
        "business_unit": [fake.word() for _ in range(100)],
        "salary": [random.randint(30000, 200000) for _ in range(100)]
    }
    df = pd.DataFrame(emp_data)
    df.to_excel("employees.xlsx", index=False)

@log_execution_time
def get_top_salary_employee():
    """
    Function to fetch the name of the employee with the highest salary.
    """
    df = pd.read_excel("employees.xlsx")
    result = df.loc[df["salary"].idxmax(), "emp_name"]
    return result

@log_execution_time
def get_top_salary_business_unit():
    """
    Function to fetch the business unit with the highest aggregated salary.
    """
    df = pd.read_excel("employees.xlsx")
    grouped = df.groupby("business_unit")["salary"].sum()
    result = grouped.idxmax()
    return result

@log_execution_time
def get_top_salary_employee_in_each_business_unit():
    """
    Function to fetch the name of the employee with the highest salary in each business unit.
    """
    df = pd.read_excel("employees.xlsx")
    result = df.loc[df.groupby("business_unit")["salary"].idxmax(), "emp_name"]
    return result.tolist()

@log_execution_time
def delete_employee_with_least_salary():
    """
    Function to delete the record of the employee with the least salary.
    """
    df = pd.read_excel("employees.xlsx")
    min_salary = df["salary"].min()
    df = df[df["salary"] != min_salary]
    df.to_excel("employees.xlsx", index=False)

@log_execution_time
def update_employee_salary(emp_name, new_salary):
    """
    Function to update the salary of an employee.
    """
    df = pd.read_excel("employees.xlsx")
    df.loc[df["emp_name"] == emp_name, "salary"] = new_salary
    df.to_excel("Employees Data.xlsx", index=False)

if __name__ == "__main__":
    create_employee_excel()
    print("Top Salary Employee:")
    print(tabulate([["",get_top_salary_employee()]],headers=["","Employee Name"],
                   tablefmt = "grid"))
    print("Top Salary Business Unit:")
    print(tabulate([["",get_top_salary_business_unit()]],headers=["","Business Unit"],
                   tablefmt = "grid"))
    print("Top Salary Employee in each Business Unit:")
    print(get_top_salary_employee_in_each_business_unit())
    # print(tabulate([["",get_top_salary_employee_in_each_business_unit()]],
    #                headers=["Business Unit","Employee Name"],tablefmt = "grid"))
    delete_employee_with_least_salary()
    update_employee_salary("Sahil Yadav", 100000)
