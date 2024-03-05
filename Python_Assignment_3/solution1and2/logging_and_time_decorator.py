"""Importing time module to get current time"""
import time

def log_execution_time(func):
    """
    Decorator to log the execution time for a function.
    This decorator logs the execution time of the decorated function, along with
    the module name, function name, and current date and time.

    Parameters:
    func (function): The function to be decorated.

    Returns:
    function: The wrapper function that logs the execution time and calls the original function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        current_date = time.strftime('%Y-%m-%d')
        current_time = time.strftime('%H:%M:%S')
        arguments = kwargs
        file_name = f"{func.__module__}{current_date}.log"
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f"{func.__module__} {func.__name__} {current_date} {current_time} {arguments}\n") #pylint: disable=line-too-long
            file.write(f"Execution time: {execution_time} seconds\n\n")
        return result
    return wrapper
