def remove_vowels(input_string):
    # Define a string containing all vowels (both lowercase and uppercase)
    vowels = "aeiouAEIOU"

    #  create a new string without vowels
    result_string = ''.join(char for char in input_string if char not in vowels)

    return result_string

# Accept input from the user
input_str = input("Enter a string: ")

# Call the function and display the result
result_str = remove_vowels(input_str)

print("Original string:", input_str)
print("String without vowels:", result_str)