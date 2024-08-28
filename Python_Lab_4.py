'''
                                                        EXPERIMENT 4
'''


#Qus-1  //Find a factorial of given number.

print("Find factorial of given number")
num=int(input("Input number you want to find factorial of: "))
fact=1
temp=num
while (temp!=0):
    fact=fact*temp
    temp=temp-1
print("Factorial of",num, "is :",fact)
print("\n")



#Qus-2  //Find whether the given number is Armstrong number.

print('Find whether the given number is Armstrong number')
num=int(input("Choose number : "))
temp=num
count = 0
sum = 0
while (temp!=0):
    temp = temp // 10
    count += 1

temp = num 
while (temp!=0):
    rem = temp % 10
    temp = temp / 10
    sum += (rem**count)
    temp=int(temp)

if (sum == num):
    print("----Armstrong Number----")
else:
    print("----Not armstrong----")
print("\n")
    
    
#Qus-3  //Print Fibonacci series up to given term.

print("Print Fibonacci series up to given term")
term=int(input("Number of term in series: "))
x=0
y=1
print("Fibonacci series is:")
print(x)
print(y)
term = term-2

while (term!=0):
    z=x+y
    x=y
    y=z
    print(z)
    term-=1
print("\n")



#Qus-4  //Write a program to find if given number is prime number or not.

print("Write a program to find if given number is prime number or not")
num = int(input("Enter a number: "))
count = 0
for i in range(2, int(num//2) + 1):
    if num % i == 0:
        count += 1
        break
if count == 0 and num > 1:
    print(f"Number {num} is a Prime number\n")
else:
    print(f"Number {num} is not a Prime number\n")
    


#Qus-5  //Check whether given number is palindrome or not. 
print("Check whether given number is palindrome or not. ")
num=int(input("Enter the number : "))
sm=0
temp=num
dig=0
while (temp!=0):
    temp=temp//10
    dig+=1
temp=num
for i in range(dig):
    temp2=temp%10
    temp=temp//10
    sm=sm*10+temp2
if(sm==num):
    print(f"Number {num} is Palindrome.\n")
else:
    print(f"Number {num} is not Palindrome.\n")



#Qus-6  //Write a program to print sum of digits. 
print("Write a program to print sum of digits. ")
num=int(input("Enter the number : "))
sum=0
temp=num
while (temp!=0):
    temp2=temp%10
    temp=temp//10
    sum=int(temp2)+sum
    print(sum)
print("Sum of digits = ",sum)
print("\n")


#Qus-6  //Count and print all numbers divisible by 5 or 7 between 1 to 100
print("Count and print all numbers divisible by 5 or 7 between 1 to 100")
for i in range(100):
    if (i%5==0) or (i%7==0):
        print(f"{i} -- is divisible by 5 or 7 :  ")
print("\n")        


#Qus-7  //Convert all lower cases to upper case in a string.
print("Convert all lower cases to upper case in a string.") 
instr = input("Enter a string: ")
outstr = instr.upper()
print(f"Uppercase version: {outstr}\n")



#Qus-8   //Print all prime numbers between 1 and 100.
print("Print all prime numbers between 1 and 100.") 
def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num//2) + 1):
        if num % i == 0:
            return False
    return True
for i in range (1,100):
    if prime(i):
        print(i)
print("\n")


#Qus-9  //Print the table for a given number

print("Print the table for a given number")
Multiplier=int(input("Enter the Multiplier : "))
Multiplicand=int(input("Enter the Multiplicand till which you want to print the table : "))
for i in range (1,Multiplicand+1):
    Product=Multiplier*i
    print(f"{Multiplier} × {i} = {Product}")