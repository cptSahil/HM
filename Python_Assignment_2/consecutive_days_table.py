"""
    Importing the the necessary libraries to run the program.
"""
from tabulate import tabulate
from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time
import week_detail

@log_execution_time
def consecutive_day_table_form():
    """
        function to store the data in the form of table.
    """
    day_info = week_detail.week_details()

    table_data = []
    for day, info in day_info.items():
        table_data.append([day, info[0], info[1], info[2], info[3], info[4]])
    table_headers = ["Name of the Day","Occurrences", "Short Form",
                     "Name in Lower","Name in Upper","Length"]
    table = tabulate(table_data, headers=table_headers, tablefmt="grid")
    return table

if __name__ == "__main__":
    table_form = consecutive_day_table_form()
    print(table_form)
