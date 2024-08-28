'''
                                                        EXPERIMENT 3
'''
import math
import cmath

#QUS-1  //Check whether given number is divisible by 3 and 5 both.

print("Check whether given number is divisible by 3 and 5 both.")
num=int(input("Take number : "))
if num%3==0 and num%5==0:
    print("Number",num,"is Divisble by both numbers\n")
else:
    print("Not divisible by both\n")



#Qus-2   //Check whether a given number is multiple of five or not.

print("Check whether a given number is multiple of five or not.")
num=int(input("Take number : "))
if num%5==0:
    print("Number",num,"is Multiple of 5\n")
else:
    print("Not a Multiple of 5\n")
    
    
    
#Qus-3  //Find the greatest among two numbers. If numbers are equal than print “numbers are equal”.

print("Find the greatest among two numbers. If numbers are equal than print “numbers are equal”.")
a=int(input("Take number 1 : "))
b=int(input("Take number 2 : "))
if a >= b:
    if a==b:
        print("Numbers are Equal")
    else:
        print("num1=",a,"is greater than num2= ",b)
else:
    print("num1=",a,"is smaller than num2= ",b)
print("\n")
    
    
#Qus-4  //Find the greatest among three numbers assuming no two values are same

print("Find the greatest among three numbers assuming no two values are same")
a=int(input("Take number 1 : "))
b=int(input("Take number 2 : "))
c=int(input("Take number 3 : "))
if a > b:
    if a > c:
        print("num1=",a,"is greatest\n")
    else:
        print("num3=",c,"is greatest\n")
else:
    if b > c:
        print("num2=",b,"is greatest\n")
    else:
        print("num3=",c,"is greatest\n")
        
        
        
#Qus-5    //Check whether the quadratic equation has real roots or imaginary roots. Display the roots

print("Check whether the quadratic equation has real roots or imaginary roots. Display the roots")
print("ax^2+bx+c=0 where a!=0")
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
D=(b*b)-(4*a*c)
d=math.sqrt(D)
di=cmath.sqrt(D)
if (D>0):
    print("Real and distinct roots\n")
    x1=(-b+d)/(2*a)
    x2=(-b-d)/(2*a)
    print("Roots are: ",x1,"and ",x2)
elif(D<0):
    print("Imaginary roots")
    x1=(-b+di)/(2*a)
    x2=(-b-di)/(2*a)
    print("Roots are: ",x1,"and \n",x2)
else:
    print("Real and same roots")
    x1=(-b+d)/(2*a)
    x2=x1
    print("Roots are: ",x1,"and ",x2)
print("\n")



#Qus-6    //Find whether a given year is a leap year or not.

print("Find whether a given year is a leap year or not")
year=int(input("Enter the year : "))
if (year%4==0):
    if (year%100==0):
        if (year%400==0):
            print(year," is leap year")
        else:
            print(year," is not leap year")
    else:
        print(year," is leap year")
else:
    print(year," is not leap year")
print("\n")


#Qus-7    //Write a program which takes any date as input and display next date of the calendar

print("Write a program which takes any date as input and display next date of the calendar")
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year:"))
if month > 12:
    month = 1
    year += 1
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if day > days_in_month[month]:
    day = day-days_in_month[month]
    month += 1       
print(f"Next date: day={day} month={month} year={year}\n")




#Qus-8     //Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects and calculate the percentage.

print("Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects and calculate the percentage")
marks = [float(input(f"Enter marks for subject {i + 1}: ")) for i in range(5)]
total_marks = sum(marks)
percentage = (total_marks / (len(marks) * 100)) * 100
cgpa = percentage / 10
if 0 <= cgpa <= 3.4:
    grade = 'F'
elif 3.5 <= cgpa <= 5.0:
    grade = 'C+'
elif 5.1 <= cgpa <= 6.0:
    grade = 'B'
elif 6.1 <= cgpa <= 7.0:
    grade = 'B+'
elif 7.1 <= cgpa <= 8.0:
    grade = 'A'
elif 8.1 <= cgpa <= 9.0:
    grade = 'A+'
elif 9.1 <= cgpa <= 10.0:
    grade = 'O'
else:
    grade = 'Invalid CGPA'
print(f"percentage: {percentage}%")
print(f"CGPA: {cgpa:.2f}")
print(f"Grade: {grade}")