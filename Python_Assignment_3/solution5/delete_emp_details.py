""""Import necessary details"""
import json
from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time

@log_execution_time
def delete_employee_by_name(business_units):#pylint: disable=redefined-outer-name
    """
    Delete multiple employees by their names whenever an employee's contract is terminated.

    Parameters:
    business_units (dict): A dictionary containing the employee data aggregated by Business Unit.

    Returns:
    list: A list of dictionaries containing details of the terminated employees.

    Raises:
    ValueError: If an employee with the provided name is not found in the business units data.
    """
    employee_names = input("Enter the names of employees to be terminated: ").split(',')
    deleted_employees = []
    for employee_name in employee_names:
        deleted = False
        for employees in business_units.values():
            for employee in employees[:]:
                if employee.get('EMP NAME') == employee_name:
                    employees.remove(employee)
                    deleted = True
                    deleted_employees.append(employee)
                    with open('Terminated_employee.json', 'a', encoding='utf-8') as file: #pylint: disable=redefined-outer-name
                        json.dump(employee, file,indent=4)
                        file.write('\n')
                    break
        if not deleted:
            raise ValueError(f"Employee with Name '{employee_name}' not found!")
    return deleted_employees

if __name__ == "__main__":
    with open('Aggregated_emp_data.json', 'r', encoding='utf-8') as file:
        business_units = json.load(file)
    try:
        terminated_emp_details = delete_employee_by_name(business_units)
        print("Terminated employees and their details:")
        for emp in terminated_emp_details:
            print(emp)
    except ValueError as e:
        print(e)
    with open('Aggregated_emp_data.json', 'w', encoding='utf-8') as file:
        json.dump(business_units, file, indent=4)
