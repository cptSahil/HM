# Assignment 3

## Description
This project consists of several modules that perform different tasks related to decorators and analyzing the data.

## Modules

### Ques 1 and 2:
- 1. Write a decorator to log the following details whenever a function is called
	a. The File needs to be name of the <module>_<YYYYMMDD>.log
	b. The messages in the logs file should follow the format as below
		<module name> <function name> <DD-MM-YY> <hh:mm:ss> <Dict of Arguments passed to the function>
- 2. Write a decorator to log the execution time for a function. The time can be logged in the same file as above.

### folder: solution1and2
#### __init__.py
#### logging_and_time_decorator.py
##### Description:
- This module contains decorators to log function calls and execution time.
##### Functions:
- `log_execution_time()`: Decorator to log function calls and execution time.

### Ques 3:
- 3. Write a decorator to validate arguments passed to a function based on a condition.
e.g. Write a WAF to generate sequence of squares of all even numbers in the range of 1 to 10
Check if the number passed as a argument is in the specified range using decorators. If the condition fails the function 
should return an exception "ValueError" with an appropriate message.

### folder: solution3
#### validating_number.py
##### Description:
- This module contains a function to generate the square of even numbers in given range.
##### Functions:
- `generate_squares_of_even_number()`: Function to generate a sequence of squares of all even numbers in a given range.

#### validating_decorator.py
##### Description:
- This module contians a decorator to validate arguments passed to a function based on certain condition.
##### Functions:
- `validate_range()`: Decorator to validate the range of arguments passed to a function.

### Ques 4:
- 4. Use the python Faker module to generate fake data for the following.
	a. Create an JSON File "Employee Personal Details" with following data. Generate around 50-100 records
		"EMP ID", "EMP NAME", "EMP EMAIL", "Businees Unit" "Salary"

### folder: solution4
#### employee_details.py
##### Description:
- This module generates fake data for employee personal details and saves it in a JSON file.
##### Functions:
- `generate_employee_data()`: Function to generate fake data for employee personal details and save it in a JSON file.

### Ques 5:
- 5. Use the above created JSON File as an input to the following
	a. Create a JSON File to aggregate the above data w.r.t Businees Unit and store the Employee details. 
	
	b. Delete multiple employee and their corresponding details whenever an employee contract is 
	   terminated and maintain the name of the employee in a separate JSON file.
	   . Raise and exception whenever you are asked to delete the employee details that is not present.

	c. Fix a salary hike in terms of percentage for each Business Unit and update the salary figures
	for all employees based on the same

### folder: solution5
#### aggregate_emp_details.py
##### Description:
- This module aggregates employee data w.r.t. Business Unit and stores the details in a JSON file.
##### Functions:
- `aggregate_employee_data()`: Function to aggregate employee data w.r.t. Business Unit and store the details in a JSON file.

#### delete_emp_details.py
##### Description:
- This module deletes multiple employees and their corresponding details from the data when an employee contract is terminated.
##### Functions:
- `delete_employee_by_name()`: Function to delete multiple employees and their corresponding details from the data.

#### hiked_salary.py
##### Description:
- This module fixes a salary hike in terms of percentage for each Business Unit and updates the salary figures for all employees based on the same.
##### Functions:
- `hike()`: Function to fix a salary hike for each Business Unit and update the salary figures for all employees.

## Dependencies
- time
- json
- pandas
- faker
- random