
def reverseWord(s, start, end):
    while start < end:
        # Swap the characters at the start and end indices
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

def reverseString(s):
    s = list(s) # Convert the input string to a list of characters
   
    # Initialize start and end indices
    start, end = 0, len(s) - 1
    reverseWord(s,start,end) # Reverse the entire string

    start = end = 0
    while end<len(s):
        # If a space is encountered, reverse the word between start and end indices
        if s[end] == ' ': 
            reverseWord(s, start, end-1) 
            start = end+1
        end += 1

    reverseWord(s, start, end-1) # Reverse the last word
    return ''.join(s)  # Convert the list of characters back to a string and return it

if __name__ == "__main__":
    input_Sting = input("Enter the Sentence: ")
    print(reverseString(input_Sting))