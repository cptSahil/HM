"""
Description:
This script defines a OrderPlacer class to manage user login and order placement.

Classes:
- OrderPlacer: Manages user login and place order according to data.

Functions/Methods:
- __init__: Initializes the LoginManager class with URL, filename, and browser manager.
- place_orders: Perform user login, place order, check criteria for success/failure and store data
in excel sheet.
"""
import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from login import Login

class OrderPlacer:
    """
    A class to place orders on a website using Selenium WebDriver.

    Attributes:
        filename (str): The name of the Excel file containing order details.
        url (str): The URL of the website to place orders on.
        browser_manager: An instance of the browser manager to handle WebDriver operations.
    """
    def __init__(self,filename,url,browser_manager):
        self.driver = webdriver.Chrome()
        self.url = url
        self.filename = filename
        self.browser_manager = browser_manager

    def place_orders(self):
        """
        Method to place orders based on data from an Excel file.

        This method iterates through rows in the Excel file, logs in, adds products to cart,
        fills in checkout information, and updates order status in the Excel file.
        """
        try:
            workbook = openpyxl.load_workbook(self.filename)
            order_sheet = workbook["Order_details"]
            order_sheet["E1"] = "Order Status"

            row_index = 2  # Start from the second row where data begins

            for row in order_sheet.iter_rows(min_row=row_index, values_only=True):
                username, product, quantity, *_ = row

                self.browser_manager.setup_browser(self.url)
                print("Opened website successfully")
                time.sleep(3)

                username_field = self.browser_manager.driver.find_element(By.ID, "user-name")
                password_field = self.browser_manager.driver.find_element(By.ID, "password")
                login_button = self.browser_manager.driver.find_element(By.CLASS_NAME, "btn_action")

                username_field.send_keys(username)
                password_field.send_keys("secret_sauce")
                login_button.click()
                # Login.login(username,"secret_sauce")
                print("Logged in successfully")

                self.driver.implicitly_wait(5)
                time.sleep(3)

                product_element = self.browser_manager.driver.find_element(By.XPATH, f"//*[text()='{product}']/../../..")
                # print(product_element)
                add_to_cart_button = product_element.find_element(By.CLASS_NAME, "btn_inventory")
                add_to_cart_button.click()
                print("Product added to cart successfully")

                time.sleep(3)

                cart_icon = WebDriverWait(self.browser_manager.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_container")))
                cart_icon.click()
                time.sleep(3)

                product_in_cart = self.browser_manager.driver.find_element(By.XPATH,"//div[@class='inventory_item_name']").text

                cart_quantity = self.browser_manager.driver.find_element(By.CLASS_NAME, "cart_quantity")
                cart_count = int(cart_quantity.text)
                print("Cart count:", cart_count)

                checkout_button = self.browser_manager.driver.find_element(By.CLASS_NAME, "checkout_button")
                checkout_button.click()
                print("Clicked on Checkout button")

                # Fill in the checkout information
                first_name_field = self.browser_manager.driver.find_element(By.ID, "first-name")
                last_name_field = self.browser_manager.driver.find_element(By.ID, "last-name")
                postal_code_field = self.browser_manager.driver.find_element(By.ID, "postal-code")

                first_name_field.send_keys("John")
                last_name_field.send_keys("Doe")
                postal_code_field.send_keys("12345")

                continue_button = self.browser_manager.driver.find_element(By.CLASS_NAME, "cart_button")
                continue_button.click()

                finish_button = self.browser_manager.driver.find_element(By.CLASS_NAME, "cart_button")
                finish_button.click()

                print(product_in_cart)
                if cart_count == int(quantity):
                    if product_in_cart == product:
                        order_sheet.cell(row=row_index, column=5, value="Success")
                        print("Order status updated to Success")
                else:
                    order_sheet.cell(row=row_index, column=5, value="Failure")
                    print("Order status updated to Failure")

                workbook.save(self.filename)
                print("Excel file saved successfully")
                time.sleep(3)
                row_index += 1
            print("All orders placed successfully!")

        finally:
            self.driver.quit()
