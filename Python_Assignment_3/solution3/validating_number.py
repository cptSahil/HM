"""Importing decorator module to validate the range"""
from validation_decorator import validate_range
from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time

@log_execution_time
@validate_range(1,10)
def generate_squares_of_even_number(num):
    """
    Generate squares of even numbers up to the given number.

    Parameters:
    num (int): The upper limit for the generating squares of even numbers.

    Returns:
    list: A list containing the squares of even numbers up to 'num'
    """
    return [num**2 for num in range(2,num+1,2)]

try:
    result_valid = generate_squares_of_even_number(10)
    print(result_valid)
except ValueError as e:
    print(e)

try:
    result_valid = generate_squares_of_even_number(15)
    print(result_valid)
except ValueError as e:
    print(e)
