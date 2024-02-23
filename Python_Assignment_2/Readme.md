#Assignment 2

## Description
This project consists of several modules that perform different tasks related to processing and analyzing data.

## Modules

### 1. week_detail.py
#### Description:
- This module provides details about the days of the week.
#### Functions:
- `week_details()`: Returns information about each day of the week, including occurrence, short name, lowercase name, uppercase name, and length of the day name.

### 2. consecutive_days.py
#### Description:
- This module generates pairs of consecutive days.
#### Functions:
- `two_consecutive_days()`: Returns a list of tuples containing consecutive pairs of days.

### 3. character_occurrence.py
#### Description:
- This module calculates the occurrence of characters in each day's name.
#### Functions:
- `get_character_tuples()`: Generates tuples containing each day's name and its character count dictionary.

### 4. employees_data.py
#### Description:
- This module handles employee data, including creating Excel files, fetching top salary information, deleting employees with the least salary, and updating employee salaries.
#### Functions:
- `create_employee_excel()`: Creates an Excel file with randomly generated employee data.
- `get_top_salary_employee()`: Returns the name of the employee with the highest salary.
- `get_top_salary_business_unit()`: Returns the business unit with the highest aggregated salary.
- `get_top_salary_employee_in_each_business_unit()`: Returns the name of the employee with the highest salary in each business unit.
- `delete_employee_with_least_salary()`: Deletes the record of the employee with the least salary.
- `update_employee_salary(emp_name, new_salary)`: Updates the salary of a specific employee.

## Usage
1. Run the main script `create_excel_file.py` to generate an Excel file containing various data.
2. View the generated Excel file `assignment_output.xlsx` to see the results.

## Dependencies
- pandas
- faker
- tabulate
- random
