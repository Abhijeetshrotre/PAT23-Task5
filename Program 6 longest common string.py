def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a table to store lengths of the common
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Variables to store the length and ending position of substring
    max_length = 0
    end_position = 0

    # Build the  table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_position = i - 1
            else:
                dp[i][j] = 0

    # Extract the longest common substring
    common_substring = str1[end_position - max_length + 1: end_position + 1]

    return common_substring

# Accept input from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Call the function and display the result
result = longest_common_substring(str1, str2)

print(f"The longest common substring between '{str1}' and '{str2}' is: '{result}'")