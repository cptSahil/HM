
def reverseWord(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

def reverseString(s):
    s = list(s)
    start, end = 0, len(s) - 1
    reverseWord(s,start,end)

    start = end = 0
    while end<len(s):
        if s[end] == ' ':
            reverseWord(s, start, end-1)
            start = end+1
        end += 1

    reverseWord(s, start, end-1)
    return ''.join(s)

if __name__ == "__main__":
    input_Sting = input("Enter the Sentence: ")
    print(reverseString(input_Sting))