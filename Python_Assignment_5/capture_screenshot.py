"""
Description:
This script defines a Screenshot class that handles taking screenshot whenever the function called.

Classes:
- Screenshot: A class to handle taking screenshots of the page.

Funtions/Modules:
- __init__: Initializes an instance of the Screenshot class with browser_manager.
- capture: Capture a screenshot of the current web page.

Dependencies:
- os: Provides a way to use operating system-dependent functionality.
- datetime: Provides a way to manipulate dates and times.
"""
import os
from datetime import datetime

class Screenshot:                       #pylint: disable=R0903
    """
    A class to capture screenshots using a provided browser manager.

    Attributes:
    - browser_manager: An instance of BrowserManager to control the web browser.
    """
    def __init__(self,browser_manager):
        """
        Initialize the Screenshot class with a BrowserManager instance.

        Parameters:
        - browser_manager: An instance of BrowserManager to control the web browser.
        """
        self.browser_manager = browser_manager

    def capture(self):
        """
        Capture a screenshot of the current web page.

        The screenshot is saved in a 'Screenshots' directory with a filename containing the
        current timestamp.

        Returns:
        - filepath (str): The path to the saved screenshot file.
        """
        if not os.path.exists('Screenshots'):
            os.makedirs("Screenshots")
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{current_time}.png"
        filepath = os.path.join('Screenshots',filename)
        self.browser_manager.driver.get_screenshot_as_file(filepath)
