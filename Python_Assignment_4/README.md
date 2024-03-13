# Python Assignment 4
This Python project manages employee data using the `Employee` class. It provides functionalities to load employee data from a JSON file, create Employee objects, and write employee data to JSON files.

##  Problem Statement:
    Use the python Faker module to generate fake data for the following.
	a. Create an JSON File "Employee Personal Details" with following data. Generate around 50-100 records
		"EMP ID", "EMP NAME", "EMP EMAIL", "Businees Unit" "Salary"
    Note: This is already done as a part of the last assignment.

    User the above as input data and do the following.

    1. Define a class for the Employee and load all the data as Objects of this class.

    2. Define setter methods for every attribute of the class.
        a. Set the value passed to it as a parameter
        b. Use Faker module to set the value as default
    
    3. Define getter methods for very attribute of the class.
    
    4. Define a method in the class to convert the Employee object to a JSON and write it to a file.
        The function should be able to do it for 
        * one employee
        * List of Employees 
        * All(by default)

## Requirements
- Python 3.x
- faker library (`pip install faker`)

## Usage
1. **Installation**: Install the faker library if you haven't already:
2. **Run the code**

## Functionality
- **Employee Class**: 
    - Represents an employee with attributes such as ID, name, email, business unit, and salary.
- **Loading Employee Data**: 
    - Load employee data from a JSON file into Employee objects.
    - Uses the faker module to set default values if data is missing.
- **Writing Employee Data**:
    - Write data for one employee to a JSON file.
    - Write data for a list of employees to a JSON file.
    - Write data for all employees to a JSON file.
- **Logging Execution Time**:
    - Utilizes a decorator to log the execution time of specific methods.

## Additional Information
- The `Employee` class provides setter methods to set the attributes of an employee with default values generated using the faker library.
- It also provides getter methods to retrieve the values of employee attributes.
- The code uses a decorator to log the execution time of certain methods.
- The logging functionality provides insights into how long each operation takes, which can help optimize