"""
    Importing the the necessary libraries to run the program
"""

from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time
import pandas as pd
import week_detail
import consecutive_days
import character_occurrence
import employees_data

@log_execution_time
def create_excel_file():
    """ 
        Create DataFrames from the week_details, consecutive_days, and character_occurrence
    """
    df1 = pd.DataFrame(week_detail.week_details()).T.reset_index()
    df1.columns = ["Name of the Day", "Occurrences", "Short Form",
                    "Name in Lower", "Name in Upper", "Length"]
    df2 = pd.DataFrame(consecutive_days.two_consecutive_days(), columns=["Start Date", "End Date"])
    df3 = pd.DataFrame(character_occurrence.get_character_tuples(),
                       columns=["Character", "Occurrences"])
    df4 = pd.DataFrame({
        "Top Salary Employee": [employees_data.get_top_salary_employee()],
        "Top Salary Business Unit": [employees_data.get_top_salary_business_unit()],
        "Top Salary Employee in each Business Unit":
        [employees_data.get_top_salary_employee_in_each_business_unit()],
        })
    # Write the DataFrames to a single Excel file, each on a separate sheet
    with pd.ExcelWriter('assignment_output.xlsx') as writer:
        df1.to_excel(writer, sheet_name='Week Details', index=False)
        df2.to_excel(writer, sheet_name='Consecutive Days', index=False)
        df3.to_excel(writer, sheet_name='Character Occurrence', index=False)
        df4.to_excel(writer, sheet_name='Employee Details', index=False)

if __name__ == "__main__":
    create_excel_file()
