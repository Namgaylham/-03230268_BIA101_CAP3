

def read_input(file_path):
    # Initialize the sum variable
    total_sum = 0
    
    # Open the file and read it line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Remove newline characters and strip whitespace
            cleaned_line = line.strip()
            
            # Check if the line has at least one character
            if cleaned_line:
                # Extract the first and last characters
                first_char = cleaned_line[0]
                last_char = cleaned_line[-1]
                
                # Check if both characters are digits
                if first_char.isdigit() and last_char.isdigit():
                    # Combine them into a two-digit number and add it to the sum
                    total_sum += int(first_char + last_char)
    
    return total_sum

# Example usage
file_path = '168.txt'  # Replace 'your_file.txt' with the path to your text file
total_sum = read_input(file_path)
print(f'The total sum of the first and last digit of each line is {total_sum}.')