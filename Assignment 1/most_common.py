"""Import the logger decorator to note date and time."""
from Python_Assignment_3.solution1and2.logging_and_time_decorator import log_execution_time

@log_execution_time
def most_common_characters(input_string):
    """
    Find and print the top three most common characters in a given string.

    Parameters:
    inputString (str): The input string to analyze.

    Returns:
    None
    """
    # Convert the input string to uppercase
    s = input_string.upper()
    freq = {}
    # Iterate through each character in the string
    for char in s:
        # If the character is already in the dictionary then increment
        if char in freq:
            freq[char] += 1
        # If the character is not in the dictionary then add it
        else:
            freq[char] = 1

    # Sort the dictionary items based on custom sort function and get top 3 most common characters
    most_common = sorted(freq.items(), key=custom_sort)[:3]

    # Iterate through the top three most common characters and their counts, then print them
    for char, count in most_common:
        print(f"Character: {char}, Count: {count}")

def custom_sort(item):
    """
    Custom sort function to sort items based on count in descending order
    and character in ascending order.

    Parameters:
    item (tuple): A tuple containing a character and its count.

    Returns:
    tuple: A tuple with count in descending order and character in ascending order.
    """
    return(-item[1],item[0])

if __name__ == "__main__":
    inputString = input('Enter the String: ')
    most_common_characters(inputString)
