################################
# Github Repo link: https://github.com/Namgaylham/-03230268_BIA101_CAP3
# Your Name: Namgay Lham
# Your Section : B
# Your Student ID Number: 03230168
################################
# REFERENCES
# https://youtu.be/Uh2ebFW8OYM?feature=shared
# https://youtu.be/ac3nbZ0V9PU?feature=shared
#https://youtu.be/OehCy8mnWX4?feature=shared
# SOLUTION
# Your Solution Score: 
################################

def calculate_sum(myfile):
    # Initialize total sum
    my_total_sum = 0
    try:
        # Open the file in read mode with automatic closing (using with open)
        with open(myfile, 'r') as file:
            # Iterate through each line in the file
            for line in file:
                # Remove leading/trailing whitespace from the line
                line = line.strip()
                # Initialize variables to store the first and last digits in the line
                first_digit = None
                last_digit = None
                # Iterate through each character in the line
                for char in line:
                    # Check if the character is a digit
                    if char.isdigit():
                        # If it's the first digit encountered in the line, store it
                        if first_digit is None:
                            first_digit = char
                        # Always update the last digit encountered in the line
                        last_digit = char
                # If both the first and last digits are found in the line, add their sum to the total sum
                if first_digit is not None and last_digit is not None:
                    my_total_sum += int(first_digit + last_digit)
    except FileNotFoundError:
        # Handle file not found error
        print("Error: File not found.")
    except Exception as e:
        # Handle any other exceptions
        print("An error occurred:", e)
    # Return the total sum
    return my_total_sum

def final():

# Entry point of the program

  if __name__ == "__main__":
    # Ask user to input the filename
    input_filename = input("Enter your input file: ")
    # Call calculate_sum function with the input filename and store the result
    result = calculate_sum(input_filename)
    # Print the final result
    print("Final Result:", result)

final()