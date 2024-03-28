"""
Description:
The script defines a ProductDetailsRetriever class to retrieve and store product details
from a web page after logging in. It captures the product details in the excel sheet

Classes:
-ProductDetailsRetriever: Retrieves and stores product details from website.

Function/Methods:
-__init__: Initializes the ProductDetailsRetriever class with URL, filename, browser manager.
-login_to_website: Logs into the website using provided username and password.

Dependencies:
- pandas: For data manipulation and Excel handling.
- selenium.webdriver.common.by.By: For locating elements on the web page.
"""
import pandas as pd
from selenium.webdriver.common.by import By
from tasks.login import Login

class ProductDetailsRetriever:                      #pylint: disable=R0903
    """
    A class to retrieve and store product details from a web page after logging in.

    Attributes:
    - browser_manager: An instance of BrowserManager to control the web browser.
    - url (str): The URL of the web page.
    - filename (str): The name of the Excel file to store product details.
    """
    user_id = "standard_user"
    password = "secret_sauce"
    product_detail = "inventory_item"

    def __init__(self, browser_manager, url, filename):
        """
        Initialize the ProductDetailsRetriever class.

        Parameters:
        - browser_manager: An instance of BrowserManager.
        - url (str): The URL of the web page.
        - filename (str): The name of the Excel file.
        """
        self.url = url
        self.filename = filename
        self.browser_manager = browser_manager

    def login_and_retrieve_product_details(self):
        """
        Log in to the web page and retrieve product details, then store them in an Excel file.
        """
        try:
            self.browser_manager.setup_browser(self.url)
            login_manager = Login(self.browser_manager,self.user_id,self.password)
            login_manager.login()

            self.browser_manager.driver.implicitly_wait(5)

            products = self.browser_manager.driver.find_elements(By.CLASS_NAME, self.product_detail)
            product_data = {"Product ID": [], "Product Name": [], "Description": [], "Price": []}

            for idx, product in enumerate(products, start=1):
                product_info = product.text.split("\n")
                product_name = product_info[0]
                product_description = product_info[1]
                product_price = product_info[2]

                product_data["Product ID"].append(idx)
                product_data["Product Name"].append(product_name)
                product_data["Description"].append(product_description)
                product_data["Price"].append(product_price)

            df = pd.DataFrame(product_data)

            with pd.ExcelWriter(self.filename, mode='a', engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Product Details', index=False)

            print("Data appended successfully to Excel file.")

        except FileNotFoundError:
            print("File not found. Please check the file path.")
