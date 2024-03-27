# Swag Labs - Automation

This repository contains a Python script for retrieving data from a Saucedemo web page.

## Requirements to fulfill
1. Retrieve all the Users and password related information and store it in Sheet named "User credentials" in a excel file.
User ID, User Name, Password

2. Try login with all the Users provided on the website link https://www.saucedemo.com/v1/ and record any error messages 
displayed for a specific user. write this information to another sheet named "Login" in the same excel file as above 
in the following format.
User ID, Login Message
 
3. Login using the "standard_user" and retrieve all the product related information for every listed product. 
Write this information into a separate sheet named "Product Details" in the same excel file.
Product ID, Product Name, Description, Price

4. Manually create another sheet called "Order Details" in the same excel file and add Orders for 
the "standard_user" and "problem_user". Decide on the Columns on your own and try to represent this data. 
(review before you move to next one)

5. Using the above "Order Details" sheet try the place all the orders on the website one by one. Update a new column in the 
"Order Details" sheet called "Order Status" marking it as "Success/Failure".
Success criteria should be as follows.
1. The correct number of items should be added to the Cart.
2. The total amount at the end should be correct.
3. Success message should be displayed for every order placed.
4. No Items should be left over in the cart.

## Overview / Requirement fulfilled

The script performs the following tasks:

1. Retrieves user credentials from a web page.
2. Logs in to the web page with the user credentials.
3. Retrieves product details from the web page.
4. Creates an order details file with the product details.
5. Updates the order details file with a new column and check the success/failure according to criteria.

The script uses several classes and functions from different modules to accomplish these tasks.

## Modules

- `retrieve_data`: Contains the `CredentialsRetriever` class to retrieve user credentials from a web page.
- `login_users`: Contains the `LoginManager` class to log in to a web page with user credentials.
- `browser`: Contains the `BrowserManager` class to control the web browser.
- `product`: Contains the `ProductDetailsRetriever` class to retrieve product details from a web page.
- `create_order_details_file`: Contains the `CreateOrderDetailsFile` class to create an order details file.
- `login`: Contains the `Login` class to use the comman login method according to the need.
- `main`: It is the main file to automate the work and run all other functionalities together.
-  `checkout_information` : Contains the `CheckoutInfo` class that contains the user details for the checkout the product. 

## Classes

- `CredentialsRetriever`: Manages the retrieval of user credentials from a web page.
- `DataManager`: Manages the login process with user credentials.
- `BrowserManager`: Manages the web browser.
- `ProductDetailsRetriever`: Manages the retrieval of product details from a web page.
- `CreateOrderDetailsFile`: Manages the creation of an order details file.
- `Login`: Manages the login the user using the  username and password.
- `CheckoutInfo` : Stores the information related to users for checkout. 

## Functions/Methods

- `setup_browser` : Function use to setup the open selected browser and get to the url.
- `close_browser` : Function use to terminate the current running browser. 
- `retrieve_user_credentials`: Retrieves user credentials from the web page and saves them to an Excel file.
- `login_with_users`: Logs in to the web page with user credentials.
- `login_and_retrieve_product_details`: Logs in to the web page and retrieves product details.
- `save_order_details`: Creates an order details file.
- `login`: Logged in the website using user credentials.
- `personal_info` : Fill the user's personal info like first name, last name etc

## Dependencies

- `pandas`: For data manipulation and Excel file handling.
- `selenium.webdriver.common.by.By`: For locating elements on the web page.
- `openpyxl` : For working with Excel files.
- `selenium.webdriver.common.keys.Keys`: For keyboard actions.
- `selenium.webdriver.support.ui.WebDriverWait`: For explicit waits.
- `selenium.webdriver.support.expected_conditions`: For defining expected conditions.
- `selenium.common.exceptions.TimeoutException`: For handling timeout exceptions.

## Setup

1. Install the required dependencies using `pip`:
`pip install -r requirement.txt`.
2. Update the `URL` and `FILENAME` variables in the script with the appropriate values.
3. Run the script.

## Usage

The script can be run with the following command:
This will perform the tasks described in the `Overview` section.

 