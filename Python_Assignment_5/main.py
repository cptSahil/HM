"""
This script demonstrates how to retrieve user credentials, log in to a web page, retrieve product 
details, create an order details file, and update the file. It uses several classes and functions
from different modules to accomplish these tasks.

Modules:
- retrieve_data: Contains the CredentialsRetriever class to retrieve user credentials from website.
- login_users: Contains the LoginManager class to log in to a web page with user credentials.
- browser: Contains the BrowserManager class to control the web browser.
- product: Contains the ProductDetailsRetriever class to retrieve product details from a web page.
- create_order_details_file: Contains the CreateOrderDetailsFile class to create an order details.
- update_file: Contains the UpdateFile class to update the order details file.
"""
from retrieve_data import CredentialsRetriever
from login_users import LoginManager
from browser import BrowserManager
from product import ProductDetailsRetriever
from create_order_details_file import CreateOrderDetailsFile
from order_result import OrderPlacer

URL = "https://www.saucedemo.com/v1/"
FILENAME = "saucedemo_credentials.xlsx"

browser_manager = BrowserManager()
login_manager = LoginManager(URL,FILENAME, browser_manager)

credentials_retriever = CredentialsRetriever(URL, FILENAME, browser_manager)
credentials_retriever.retrieve_user_credentials()
browser_manager.close_browser()

login_manager.login_with_users()
browser_manager.close_browser()

product_manager = ProductDetailsRetriever(browser_manager,URL, FILENAME)
product_manager.login_and_retrieve_product_details()
browser_manager.close_browser()

create_order_manager = CreateOrderDetailsFile(FILENAME)
create_order_manager.save_order_details()

order_details_data = [['standard_user','Sauce Labs Bolt T-Shirt',1,15.99],
                        ['problem_user','Sauce Labs Bike Light',1,9.99],
                        ['standard_user','Sauce Labs Bike Light',1,9.99],
                        ['problem_user','Sauce Labs Onesie',1,7.99]]

create_order_manager.add_order_data(order_details_data)
browser_manager.close_browser()

order_placer = OrderPlacer(FILENAME,URL,browser_manager)
order_placer.place_orders()
browser_manager.close_browser()
