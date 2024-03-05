"""importing psutil module"""
import psutil
from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time

# Define a function to count the number of running instances of a specified process name
@log_execution_time
def instances(process_name):
    """
    Count the number of running instances of a specified process name.

    Parameters:
    processName (str): The name of the process to count instances of.

    Returns:
    int: The number of running instances of the specified process name.
    """
    count = 0 # initalize the count variable

    running_applications = psutil.process_iter(['name'])

    # Iterate through each Process in monitor
    for proc in running_applications:
        if proc.info['name'] == process_name:
            count += 1

            # If the no of running instances exceeds the maximum allowed instances, kill the process
            if count > 2:
                proc.kill()
    return count

# Define a function to monitor the running instances of specified applications
def monitor_applications():
    """
    Monitor the running instances of specified applications.

    Parameters:
    None

    Returns:
    None
    """
    for app in applications:
        process_name = app['processName']
        max_instances = app['maxInstances']

        # Count the number of running instances of the application
        running_instances = instances(process_name)

        # If the number of running instances exceeds the maximum allowed instances
        if running_instances > max_instances:
            print(f'Warning: More than {max_instances} instances of {process_name} running!')
         # Otherwise, print the number of running instances
        else:
            print(f'{process_name}: {running_instances}/{max_instances}')

# Define a list of applications to monitor
applications = [
    {'processName': "chrome.exe",'maxInstances': 2},
    {'processName': "notepad.exe",'maxInstances': 2,},
    {'processName': "calc.exe",'maxInstances': 2},
    {'processName': "msedge.exe",'maxInstances': 2}
]

if __name__ == "__main__":
    monitor_applications()
