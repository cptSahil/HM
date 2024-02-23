"""
    Function to get the character occurance in the each day's name.
"""
def count_characters(day):
    """
    count the occurrences of each character in the given day's name.
    """
    char_count = {}
    for char in day.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_character_tuples():
    """
    Generate tuples containing each day's name and its character count dictionary.
    """
    days_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    result = []
    for day in days_names:
        count_dict = count_characters(day)
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        char_dict = {}
        for char, count in sorted_counts:
            char_dict[char] = count
        char_tuple = (day, char_dict)
        result.append(char_tuple)
    return tuple(result)

if __name__ == "__main__":
    character_occur = get_character_tuples()
    print(character_occur)
