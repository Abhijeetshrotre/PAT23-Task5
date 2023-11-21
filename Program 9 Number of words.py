def count_words(input_string):
    # Split the string into a list of words using whitespace
    words = input_string.split()

    # Return the number of words
    return len(words)


# Get input from the user
user_input = input("Enter a string: ")

# Call the function and print the result
result = count_words(user_input)
print(f"The number of words in the string is: {result}")