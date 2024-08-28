#Qus 1   Add few names, one name in each row, in “name.txt file”.
print("Add few names, one name in each row, in “name.txt file”.")
with open('name.txt', 'w') as file:
    file.write('Shailendra Rathaur\n')
    file.write('Priyam Ranavat\n')
    file.write('Somya Pratap Singh\n')
    file.write('Ujjwal Tiwary\n')
    
    
with open("name.txt", "r") as file:
    names = file.readlines()
    num_names = len(names)
    vowel_count = sum(1 for name in names if name[0].lower() in 'aeiou')
    longest_name = max(names, key=len).strip()
    
print(f"Count of number of name : {num_names}")
print(f"{vowel_count} :  starting with vowels")
print(f"longest name : {longest_name}")


#Qus-2  Store integers in a file. (a. Find the max number, b. Find average of all numbers,  c. Count number of numbers greater than 100 )
print("\n\nCount number of numbers greater than 100")
with open('numbers.txt', 'w') as file:
    file.write('50\n')
    file.write('100\n')
    file.write('150\n')
    file.write('125\n')
    file.write('75\n')

with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]
    max_number = max(numbers)
    average = sum(numbers) / len(numbers)
    greater_than_100 = sum(1 for num in numbers if num > 100)

print(f"Maximum number: {max_number}")
print(f"Average: {average}")
print(f"Number of numbers greater than 100: {greater_than_100}")


#Qus-3  Assume a file city.txt with details of 5 cities in given format (Open file city.txt and read to, display city detals,sum of area etc)




#Qus-4  Input two values from user where the first line contains N, the number of test cases. The next N lines contain the space separated values of a and b. Performinteger division and print a/b. Handle exception in case of ZeroDivisionError or ValueError.
def create_file(newfile, test_cases):
    with open(newfile, 'w') as f:
        f.write(str(test_cases) + '\n')                                                             # Writing the number of test cases to the file
        for _ in range(test_cases):
            a = input("Enter value of a for test case {}: ".format(_ + 1))
            b = input("Enter value of b for test case {}: ".format(_ + 1))
            f.write(a + ' ' + b + '\n')                                                              # Writing a and b for each test case to the file


def division(input_file, output_file):
    with open(input_file, 'r') as f_input, open(output_file, 'w') as f_output:
        lines = f_input.readlines()                                                                 # Reading all lines from the input file
        for line in lines[1:]:                                                                      # Skipping the first line as it contains the number of test cases
            try:
                a, b = map(int, line.split())                                                       # Taking space-separated input values of a and b
                result = a // b                                                                     # Performing integer division
                f_output.write(str(result) + '\n')                                                  # Writing the result to the output file
            except ZeroDivisionError:                                                               # Handling division by zero error
                f_output.write("Error Code: integer division or modulo by zero\n")
            except ValueError:                                                                      # Handling invalid literal error (e.g., non-integer input)
                f_output.write("Error Code: invalid literal for int() with base 10: {}\n".format(b))


def main():
    test_cases = int(input("Enter the number of test cases: "))
    input_file = "input.txt"
    output_file = "output.txt"

    create_file(input_file, test_cases)                                                             # Creating the input file
    print("Input file '{}' has been created.".format(input_file))

    division(input_file, output_file)                                                               # Performing integer division and writing to output file
    print("Output has been written to '{}'".format(output_file))


if __name__ == "__main__":
    main()




#Qus-5  Create multiple suitable exceptions for a file handling program.
print("Create multiple suitable exceptions for a file handling program.")

