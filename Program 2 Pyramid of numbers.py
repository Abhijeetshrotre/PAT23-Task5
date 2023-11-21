
def create_pyramid(rows):
    num = 1
    for i in range(1, rows + 1):
        # Print spaces
        for j in range(rows - i):
            print(" ", end=" ")
        # Print ascending numbers
        for k in range(1, i + 1):
            print(num, end=" ")
            num += 1
            if num > 19:
                break
        # Print descending numbers
        for l in range(i - 1, 0, -1):
            print(num, end=" ")
            num += 1
            if num > 19:
                break
        # Move to the next line after each row
        print()
        if num > 20:
            break

# Set the number of rows for the pyramid
num_rows = 5

# Call the function to create the pyramid
create_pyramid(num_rows)