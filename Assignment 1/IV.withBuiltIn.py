def reverseSenntence(String):
    words = String.split(' ')
    reverse_Sentence = ' '.join(reversed(words))
    return reverse_Sentence

if __name__ == "__main__":
    input_String = input("Enter the Sentence: ")
    print(reverseSenntence(input_String))