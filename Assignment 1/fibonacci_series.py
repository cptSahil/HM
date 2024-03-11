"""Importing logger decorater to log the details of the function"""
from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time

class FibonacciNumber:
    """
    A class to generate a Fibonacci sequence up to the nth number.

    Attributes:
    None
    """
    def __init__(self) -> None:
        """
        Initializes the FibonacciLogger class.
        """

    @log_execution_time
    def fibonacci(self,n):
        """
        Generate a Fibonacci sequence up to the nth number.

        Parameters:
        n (int): The number of Fibonacci numbers to generate.

        Returns:
        list: A list containing the Fibonacci sequence up to the nth number.
        """
        num1, num2 = 0, 1 # Initialize the first two numbers in the sequence
        count = 0
        fib = []

        if n <= 0:
            return "Please enter a positive integer!"
        if n == 1:
            fib.append(num1)
        else:
            while count < n:
                fib.append(num1)
                nth = num1 + num2 # Compute the next number in the sequence
                num1 = num2
                num2 = nth
                count += 1
        return fib

if __name__ == "__main__":
    fib_num = FibonacciNumber()
    input_value = int(input("Enter the number: "))
    print(fib_num.fibonacci(input_value))
