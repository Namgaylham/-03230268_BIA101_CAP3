#import re
# open the text file  
#file = open('168.txt') 
  
# read the content of the text file opened 
#line = file.readlines() 
  
#to  read  line from the file 
#print(line[9]) 

# to extract integer from the line
#mixed = line[2]
#numbers = "[0-9]+"
#print(re.findall(numbers, mixed))



import re

# Open the text file (consider using a context manager for proper handling)
file = open('168.txt', 'r')

# Process each line to extract digits and calculate the sum
total_sum = 0
for line in file:
  # Extract first and last digits efficiently using slicing and regex (optional)
  first_digit = line[0:3] if line[0:3].isdigit() else None  # Check if first char is digit
  last_digit_match = re.search(r'\d$', line)  # Find the last digit
  last_digit = last_digit_match.group(0) if last_digit_match else None

  # Combine digits and add to sum only if both digits are found
  if first_digit is not None and last_digit is not None:
    two_digit_number = int(first_digit + last_digit)
    total_sum += two_digit_number

# Close the file (using context manager is recommended)
file.close()  # Close the file explicitly for clarity

# Print the total sum
print(f"The sum of two-digit numbers extracted from '168.txt' is: {total_sum}")
