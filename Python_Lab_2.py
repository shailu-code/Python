'''
                                                        EXPERIMENT 2
'''
import math                                                #importing math library ???  ask mam???


#Qus-1
x = 9
y = 7
add = x + y                                               #Addition
subtract = x - y                                          #Subtraction
multi = x * y                                             #Multiplication
div = x / y                                               #Division

print(add)
print(subtract)
print(multi)
print(div)



#Qus-2   //Write a Program where the radius is taken as input to compute the area of a circle
radius = int(input("Enter radius: "))                       #Type 1
area = 3.14 * radius * radius
print(area)

radius = float(input("Enter Radius: "))                     #type-2 
area= math.pi*(radius**2)
print("Area of circle: ",area)
print("\n")



#Qus-3  //Write a Python program to solve (x+y)*(x+y)
x=int(input("Enter Number 1: "))
y=int(input("Enter Number 2: "))
solve = (x+y)*(x+y)                                         #Type 1
print("Solution of qus 3 - ",solve)

solve = ((x+y)**2)                                          #Type 2
print("Solution of qus 3 - ",solve)
print("\n")



#Qus-4   //Write a program to compute the length of the hypotenuse (c) of a right triangle using Pythagoras theorem.
base=float(input("Base of Triangle: "))
height=float(input("Height of Triangle: "))

hypo=(((base**2)+(height**2))**0.5)
print("Length of Hypotenuse :",hypo)                        #Type 1

hypo=math.sqrt((base**2)+(height**2))
print("Length of Hypotenuse :",hypo)                        #Type 2  - Using Square-root function
print("\n")



#Qus-5  //Write a program to find simple interest.
p=float(input("Principle: "))
r=float(input("Rate: "))
t=float(input("Time in years: "))
S_I=(p*r*t)/100
print("Simple Intrest: ",S_I)
print("\n")



#Qus-6  //Write a program to find area of triangle when length of sides are given.
Length=float(input("Length of Rectangle: "))                #Area of Rectangle
Breadth=float(input("Breadth of Rectangle: "))
area = Length * Breadth
print("Area of Rectangle : ",area)

a = float(input("Enter the length of side a: "))            #Area of Triangle
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Area of the triangle:", area)
print("\n")



#Qus-7  //Write a program to convert given seconds into hours, minutes and remaining seconds.
seconds = int(input("Enter the time in seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
print(f"{hours} hours, {minutes} minutes, and {remaining_seconds} seconds\n")



#Qus-8   //Write a program to swap two numbers without taking additional variable.
a=float(input("choose number 1: "))
b=float(input("Choose number 2: "))
a = a + b
b = a - b
a = a - b
print("number 1:",a)
print("number 2:",b)
print("\n")



#Qus-9   //Write a program to find sum of first n natural numbers.
n = int(input("choose Number to find sum upto that number: "))
sum = (n*(n+1))/2
print("Sum of first",n, "Natural Numbers: ",sum)
print("\n")



#Qus-10  //Write a program to print truth table for bitwise operators( & , | and ^ operators)
a = int(input("Enter the first binary number (0 or 1): "))
b = int(input("Enter the second binary number (0 or 1): "))
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)

a = int(input("Enter the 1st Number: "))
b = int(input("Enter the 2nd Number: "))
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("\n")



#Qus-11   //Write a program to find left shift and right shift values of a given number.
num = int(input("Enter a number: "))
shift= int(input("Enter the shift value: "))

left_shift = num << shift                                       #Value will get increased
right_shift = num >> shift                                      #value will get decreased

print("Left shift result:", left_shift)
print("Right shift result:", right_shift)
print("\n")



#Qus-12  //Using membership operator find whether a given number is in sequence
num = int(input("Enter a number to check membership: "))
sequence = [10, 20, 56, 78, 89]
if num in sequence:
    print(f"{num} is in the sequence.")
else:
    print(f"{num} is not in the sequence.")
print("\n")



#Qus-13   //Using membership operator find whether a given character is in a string.
char = input("Enter a character to check membership: ")
string = "Hello, i am shailendra Rathaur from Kannauj Uttar Pradesh"

if char in string:
    print(f"{char} is in the string.")
else:
    print(f"{char} is not in the string.")















