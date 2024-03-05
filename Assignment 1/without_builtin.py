"""Importing loggger file to now time and module details of logging"""
from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time

def reverse_word(s, start, end):
    """
    Reverse a word within a string from the start to end indices.

    Parameters:
    s (list): The list of characters representing the string.
    start (int): The starting index of the word to be reversed.
    end (int): The ending index of the word to be reversed.

    Returns:
    None
    """
    while start < end:
        # Swap the characters at the start and end indices
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

@log_execution_time
def reverse_string(s):
    """
    Reverse words in a sentence while maintaining their order.

    Parameters:
    s (str): The input sentence to reverse.

    Returns:
    str: The reversed sentence.
    """
    s = list(s) # Convert the input string to a list of characters

    # Initialize start and end indices
    start, end = 0, len(s) - 1
    reverse_word(s,start,end) # Reverse the entire string

    start = end = 0
    while end<len(s):
        # If a space is encountered, reverse the word between start and end indices
        if s[end] == ' ':
            reverse_word(s, start, end-1)
            start = end+1
        end += 1

    reverse_word(s, start, end-1) # Reverse the last word
    return ''.join(s)  # Convert the list of characters back to a string and return it

if __name__ == "__main__":
    input_Sting = input("Enter the Sentence: ")
    print(reverse_string(input_Sting))
