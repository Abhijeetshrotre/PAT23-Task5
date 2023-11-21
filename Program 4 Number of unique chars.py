def count_unique_characters(input_string):
    # Use a set to store unique characters
    unique_characters = set(input_string)

    # Count the number of unique characters
    count = len(unique_characters)

    return count

# Accept input from the user
input_str = input("Enter a string: ")

# Call the function and display the result
unique_char_count = count_unique_characters(input_str)

print("Number of unique characters:", unique_char_count)