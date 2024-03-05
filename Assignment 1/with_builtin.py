"""Importing loggger file to now time and module details of logging"""
from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time

@log_execution_time
def reverse_senntence(string):
    """
    Reverse a sentence by splitting it into a list of words, reversing the list, 
    and joining the words back into a sentence.

    Parameters:
    string (str): The input sentence to reverse.

    Returns:
    str: The reversed sentence.
    """
    # Split the input string into a list of words
    words = string.split(' ')

    # Reverse the list of words using the `reversed()` function and join them back into a string
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence

if __name__ == "__main__":
    input_string = input("Enter the Sentence: ")
    print(reverse_senntence(input_string))
