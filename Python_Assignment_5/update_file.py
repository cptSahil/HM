"""
Description:
The scripts define a UpdateFile class which append the additional column to the
existing excel sheet.

Classes:
- UpdateFile: Update an existing Excel file with additional information.

Functions/Methods:
- __init__: Initializes the UpdateFile class with URL, filename, and browser manager.
- add_header: Add column name for the existing excel sheet.

Dependencies:
- pandas: For data manipulation and Excel handling.
- openpyxl: For working with Excel files.
"""
import pandas as pd
import openpyxl

class UpdateFile:                       #pylint: disable=R0903
    """
    A class to update an existing Excel file with additional information.

    Attributes:
    - url (str): The URL of the web page.
    - filename (str): The name of the Excel file to be updated.
    - browser_manager: An instance of BrowserManager for web interaction.
    - workbook: The openpyxl workbook object for the Excel file.
    """

    def __init__(self, url, filename, browser_manager):
        """
        Initialize the UpdateFile class.

        Parameters:
        - url (str): The URL of the web page.
        - filename (str): The name of the Excel file.
        - browser_manager: An instance of BrowserManager.
        """
        self.filename = filename
        self.browser_manager = browser_manager
        self.url = url
        self.workbook = openpyxl.load_workbook(self.filename)

    def add_column(self):
        """
        Add a new column 'Order Status' to the 'Order_details' sheet in the Excel file.
        """
        df = pd.read_excel(self.filename, sheet_name='Order_details')
        df['Order Status'] = None

        with pd.ExcelWriter(self.filename, engine='openpyxl', mode='a', if_sheet_exists="overlay") as writer:           #pylint: disable=C0301
            df.to_excel(writer, sheet_name='Order_details', index=False)
