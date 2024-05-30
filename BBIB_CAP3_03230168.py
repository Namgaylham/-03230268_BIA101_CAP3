def calculate_sum(filename):
    total_sum = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                first_digit = None
                last_digit = None
                for char in line:
                    if char.isdigit():
                        if first_digit is None:
                            first_digit = char
                        last_digit = char
                if first_digit is not None and last_digit is not None:
                    total_sum += int(first_digit + last_digit)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", e)
    return total_sum

def main():
    input_filename = input("Enter the input file name: ")
    result = calculate_sum(input_filename)
    print("Total sum:", result)

if __name__ == "__main__":
    main()
