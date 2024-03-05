# Assignment 2

## Description
This assignment consists of several modules that perform different tasks related to processing and analyzing data.

## Modules

### Ques 1:
- 1. Create a Tuple with all Days of the week starting from Monday and output the following
	a. A list of tuples which has the two consequtive days grouped together
	b. A dictionary which has the name of the day as the key and value as a tuple with following values
		i. Occurence of the day in a week (e.g. 1 for Monday, 2 for Tuesday)
		ii. Short form of the day (first three letters)
		iii. name of the day in the lower case
		iv. name of the day in the upper case
		v. length of each name

	c. A tuple with all the characters and their number of occurences in each name of the day.

### 1. week_detail.py
#### Description:
- This module provides details about the days of the week.
#### Functions:
- `week_details()`: Returns information about each day of the week, including occurrence, short name, lowercase name, uppercase name, and length of the day name.

### Ques 2:
- 2. Using the Dictionary output from assignment 1.b print the output as a Table. The Headers of a Table are as follows
"Name of the Day", "Occurences", Short Form", "Name in Lower", "Name in upper", "Length"

### 2. consecutive_days.py
#### Description:
- This module generates pairs of consecutive days.
#### Functions:
- `two_consecutive_days()`: Returns a list of tuples containing consecutive pairs of days.

### Ques 3:
- Write the output table from assignment 2 into an Excel File (not CSV).

### 3. character_occurrence.py
#### Description:
- This module calculates the occurrence of characters in each day's name.
#### Functions:
- `get_character_tuples()`: Generates tuples containing each day's name and its character count dictionary.

### Ques 4:
- 4. Use the python Faker module to generate fake data for the following.
	a. Create an excel sheet "Employee Personal Details" with following data. Generate around 50-100 records
		"EMP ID", "EMP NAME", "EMP EMAIL", "Businees Unit" "Salary"

	4a. WAF to return the empolyee name with top most salary
	4b. WAF to return the Business Unit with top most aggregated salary
	4c. WAF to return the employee name in each Business Unit with top most salary
	4d. WAF Delete the Record of the Employee name from the Excel File with the least salary.
	4e. WAF to Update the Salary Details of an Employee in the Excel File

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
