def count_vowels(string):
    # Convert the string to lowercase
    string = string.lower()

    # Initialize count for each vowels
    total_vowels = 0
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0


    for char in string:
        # Check if the character is a vowel
        if char in "aeiou":
            total_vowels += 1
            # Update individual vowel counts
            if char == 'a':
                count_a += 1
            elif char == 'e':
                count_e += 1
            elif char == 'i':
                count_i += 1
            elif char == 'o':
                count_o += 1
            elif char == 'u':
                count_u += 1

    # Display the results
    print("Total number of vowels:", total_vowels)
    print("Count of each individual vowel:")
    print("A:", count_a)
    print("E:", count_e)
    print("I:", count_i)
    print("O:", count_o)
    print("U:", count_u)

# Enter the string for counting Vowels
input_string = input("Enter a string: ")
count_vowels(input_string)