def mostCommonCharacters(inputString):
    charCount = {}
    for char in inputString:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1

    mostCommon = sorted(charCount.items(), key=lambda x: (-x[1], x[0]))[:3]

    for char, count in mostCommon:
        print(f"Character: {char}, Count: {count}")

if __name__ == "__main__":
    inputString = input('Enter the String: ')
    mostCommonCharacters(inputString)