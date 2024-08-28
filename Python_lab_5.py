

#Qus-1   //Write a program to count and display the number of capital letters in a given string.
print("Write a program to count and display the number of capital letters in a given string.")

input_string = input("Enter a string: ")
count = 0
for char in input_string:
    if char.isupper():
        count += 1
        print(char)
print("Number of capital letters:", count)


#Qus-2   //Count total number of vowels in a given string.
print("Count total number of vowels in a given string.")
input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in input_string:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

#Qus-3   //Input a sentence and print words in separate lines.
print("Input a sentence and print words in separate lines.")
sentence = input("Enter a sentence: ")
for i in sentence:
    print(i)

#Qus-4  //WAP to enter a string and a substring. You have to print the number of times that
#       //the substring occurs in the given string. String traversal will take place from left to
#       // right, not from right to left.
print("WAP to enter a string and a substring.")
main_string = input("Enter the main string: ")
substring = input("Enter the substring: ")
count = 0
start_index = 0

while start_index < len(main_string):
    index = main_string.find(substring, start_index)
    if index == -1:
        break
    count += 1
    start_index = index + 1

print("Number of occurrences:", count)

#Qus-5   //Given a string containing both upper and lower case alphabets. Write a Python
#       //program to count the number of occurrences of each alphabet (case insensitive)
#     //and display the same.
print(" Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same.")
input_string = input("Enter a string: ")
counts = {}
for char in input_string:
    if char.isalpha():
        char = char.upper()
        counts[char] = counts.get(char, 0) + 1

for char, count in counts.items():
    print(f"{count}--{char}")

#qus-6  //Program to count number of unique words in a given sentence using sets.
print("Program to count number of unique words in a given sentence using sets.")
sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))



#Qus-7  //Create 2 sets s1 and s2 of n fruits each by taking input from user
print("Create 2 sets s1 and s2 of n fruits each by taking input from user")
s1 = {"Apple", "Mango", "orange", "Berry"}
s2 = {"Guava", "Berry", "Pineapple"}

# a) Fruits which are in both sets s1 and s2
common_fruits = s1.intersection(s2)
print("Common fruits:", common_fruits)

# b) Fruits only in s1 but not in s2
unique_s1 = s1.difference(s2)
print("Fruits only in s1:", unique_s1)

# c) Count of all fruits from s1 and s2
total_fruits = s1.union(s2)
print("Total count of fruits:", len(total_fruits))
