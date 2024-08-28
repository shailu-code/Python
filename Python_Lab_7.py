print("            Experiment-7     \n")

#Qus-1 Find the maximum and minimum numbers from a sequence of numbers. 
print("\n---Find the maximum and minimum numbers from a sequence of numbers---\n")

def max_min(numbers):
    if len(numbers)==0:  
        print("empty list")
    
    max_num = min_num = numbers[0]
    
    for num in numbers:                                                     #Iterate through the list to find the maximum and minimum numbers
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    return max_num, min_num

sequence= input("Enter the sequence of numbers separated by space: ")       #Take input sequence of numbers from the user
numbers = [int(num) for num in sequence.split()]                            #Using the split() method to split the string into a list of substrings based on spaces

maximum, minimum = max_min(numbers)                                         #Call the function to find the maximum and minimum numbers
print("Maximum number:", maximum)                                           # Display the results
print("Minimum number:", minimum)



#Qus-2 Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number
print("\n---takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number---\n")
def sum_of_cubes(n):
    if n <= 0:
        return 0
    sum_cubes = 0
    for i in range(1, n):
        sum_cubes += i**3
    return sum_cubes

n = int(input("Enter a positive integer: "))
print("Sum of cubes:", sum_of_cubes(n))



#Qus-3 Write a Python function to print 1 to n using recursion. (Note: Do not use loop)
print("\n---To print 1 to n using recursion---\n")
def print_numbers(n):
    if n < 1:
        return
    print_numbers(n - 1)
    print(n)

n = int(input("Enter a positive integer: "))
print("Numbers 1 to n:")
print_numbers(n)
    
    

#Qus-4 Write a recursive function to print Fibonacci series up to n terms
print("\n---Recursive function to print Fibonacci series up to n terms---\n")
def fibonacci(n, a=0, b=1):
    if n <= 0:
        return
    print(a, end=" ")
    fibonacci(n - 1, b, a + b)

n = int(input("Enter the number of terms for Fibonacci series: "))
print("Fibonacci series:")
fibonacci(n)
    
    

#Qus-5 Write a lambda function to find the volume of a cone
print("\n\n---lambda function to find the volume of a cone---\n")
cone_volume = lambda r, h: (1/3) * 3.14159 * r**2 * h

r = float(input("Enter the radius of the cone: "))
h = float(input("Enter the height of the cone: "))
print("Volume of cone:", cone_volume(r, h))


#Qus-6 Write a lambda function which gives a tuple of max and min from a list.
print("\n---lambda function which gives a tuple of max and min from a list---\n")
get_max_min = lambda lst: (max(lst), min(lst))

sample_input = list(map(int, input("Enter a sequence of numbers separated by space: ").split()))
print("Max and Min from list:", get_max_min(sample_input))



#Qus-7 Functions to explain mentioned concepts
print("\n---Functions to explain mentioned concepts: ---\n")

print("---Keyword argument---")
def greet(name, message="Hello"):
    print(f"{message}, {name}!")
greet("Shailendra Rathaur")  
greet("Rahul", message="Hi")


print("\n---Default argument---")
def multiply(a, b=2):
    return a * b

# Example usage:
x=int(input("what number you want to multilpy with 2: "))
print(multiply(x))
y=int(input("another number you want multiply with previous number"))
print(multiply(x,y))


print("\n---Variable-length argument---")
def average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

# Example usage:
print(average(1, 2, 3, 4, 5))