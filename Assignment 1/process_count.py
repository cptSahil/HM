"""Importing importing module to complete the task."""
import csv
import psutil
from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time

@log_execution_time
def save_process_counts_to_csv(file_name='process_counts.csv'):
    """
    Get the count of each running process and save the information to a CSV file.

    Parameters:
    file_name (str): The name of the CSV file to save the process counts.

    Returns:
    None
    """
    process_count = {}

    # Get all processes
    processes = psutil.process_iter()

    # Iterate through each process
    for proc in processes:
        process_name = proc.name()
        process_count[process_name] = process_count.get(process_name, 0) + 1

    # Save process counts to a CSV file
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Process Name', 'Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for process_name, count in process_count.items():
            writer.writerow({'Process Name': process_name, 'Count': count})
    print(f"Process count information has been saved to {file_name}")

if __name__ == "__main__":
    save_process_counts_to_csv()
