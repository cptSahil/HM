def reverseSenntence(String):
    # Split the input string into a list of words
    words = String.split(' ')

    # Reverse the list of words using the `reversed()` function and join them back into a string
    reverse_Sentence = ' '.join(reversed(words))
    return reverse_Sentence

if __name__ == "__main__":
    input_String = input("Enter the Sentence: ")
    print(reverseSenntence(input_String))