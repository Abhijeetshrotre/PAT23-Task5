def most_frequent_character(input_string):
    char_frequency = {}

    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    most_frequent_char = max(char_frequency, key=char_frequency.get)

    return most_frequent_char

# Get input from the user
user_input = input("Enter a string: ")
result = most_frequent_character(user_input)
print(f"The most frequent character is: {result}")