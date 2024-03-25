"""
Description:
A class to handle login functionality on a website using Selenium WebDriver.

Classes:
- Login:

Functions/Methods:
- __init__: Initializes the Login class with browser manager.
-login: Open the specific URL and login username and password.

Dependencies:
- selenium.webdriver.common.by.By: For locating elements on the web page.
"""
from selenium.webdriver.common.by import By

class Login:
    """
    A class to handle login functionality on a website using Selenium WebDriver.

    Attributes:
        browser_manager: An instance of the browser manager to handle WebDriver operations.
    """
    def __init__(self, browser_manager):
        """
        Initialize the Login class.

        Parameters:
        - browser_manager: An instance of Login.
        """
        self.browser_manager = browser_manager

    def login(self, username, password):
        """
        Method to log in with the provided username and password.

        Args:
            username (str): The username to log in with.
            password (str): The password corresponding to the username.

        This method finds the username, password fields, and login button on the webpage,
        fills in the provided credentials, and clicks on the login button.
        """
        username_field = self.browser_manager.driver.find_element(By.ID, "user-name")
        password_field = self.browser_manager.driver.find_element(By.ID, "password")
        login_button = self.browser_manager.driver.find_element(By.CLASS_NAME, "btn_action")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        print("Logged in successfully")
