def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for  comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Get input from the user
user_input1 = input("Enter the first string: ")
user_input2 = input("Enter the second string: ")

# Check if the strings are anagrams
result = are_anagrams(user_input1, user_input2)

# Print the result
if result:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")