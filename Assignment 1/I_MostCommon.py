def mostCommonCharacters(inputString):
    # Convert the input string to uppercase 
    S = inputString.upper()
    freq = {} # initialize an empty dictionary
    
    # Iterate through each character in the string
    for char in S:
        # If the character is already in the dictionary then increment 
        if char in freq:
            freq[char] += 1
        # If the character is not in the dictionary then add it
        else:
            freq[char] = 1

    # Sort the dictionary items based on the custom sort function and get the top three most common characters
    mostCommon = sorted(freq.items(), key=customSort)[:3]

    # Iterate through the top three most common characters and their counts, then print them
    for char, count in mostCommon:
        print(f"Character: {char}, Count: {count}")

# Define a custom sort function that sorts the items based on count in descending order and character in ascending order
def customSort(item):
    return(-item[1],item[0])

if __name__ == "__main__":
    inputString = input('Enter the String: ')
    mostCommonCharacters(inputString)