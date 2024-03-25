"""
Description:
This script defines a CredentialsRetriever class to retrieve user credentials from a web page 
and save them to an Excel file. It utilizes a BrowserManager instance to control the web browser 
and extracts user IDs, names, and passwords from specific elements on the page.

Classes:
- CredentialsRetriever: Manages the retrieval and storage of user credentials.

Functions/Methods:
- __init__: Initializes the CredentialsRetriever class with URL, filename, and browser manager.
- retrieve_user_credentials: Retrieves user credentials from the web page and saves them to an 
Excel file.

Dependencies:
- pandas: For data manipulation and Excel file handling.
- selenium.webdriver.common.by.By: For locating elements on the web page.
"""

import pandas as pd
from selenium.webdriver.common.by import By

class CredentialsRetriever:                                      #pylint: disable=R0903
    """
    A class to retrieve user credentials from a web page and save them to an Excel file.

    Attributes:
    - url (str): The URL of the web page to retrieve credentials from.
    - filename (str): The name of the Excel file to save the credentials.
    - browser_manager: An instance of BrowserManager to control the web browser.
    - credentials_data (dict): Dictionary to store user credentials data.
    """

    def __init__(self, url, filename, browser_manager):
        """
        Initialize the CredentialsRetriever class.

        Parameters:
        - url (str): The URL of the web page.
        - filename (str): The name of the Excel file.
        - browser_manager: An instance of BrowserManager.
        """
        self.url = url
        self.filename = filename
        self.browser_manager = browser_manager
        self.credentials_data = {"User ID": [], "User Name": [], "Password": []}

    def retrieve_user_credentials(self):
        """
        Retrieve user credentials from the web page and save them to an Excel file.
        """
        self.browser_manager.setup_browser(self.url)
        users = self.browser_manager.driver.find_elements(By.CLASS_NAME, "login_credentials")
        passwords = self.browser_manager.driver.find_elements(By.CLASS_NAME, "login_password")

        for user, password in zip(users, passwords):
            user_info = user.text.split("\n")
            pass_info = password.text.split("\n")
            for info, info2 in zip(user_info[1:], pass_info[1:]*len(user_info[1:])):
                self.credentials_data["User ID"].append(len(self.credentials_data["User ID"]) + 1)
                self.credentials_data["User Name"].append(info)
                self.credentials_data["Password"].append(info2)

        credentials_df = pd.DataFrame(self.credentials_data)
        credentials_df.to_excel(self.filename, sheet_name="User_credentials", index=False)
