def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for comparison
    cleaned_string = ''.join(input_string.split()).lower()

    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Accept input from the user
input_str = input("Enter a string: ")

# Call the function and display the result
result = is_palindrome(input_str)

if result:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")