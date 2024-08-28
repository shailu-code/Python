

#Qus-1  //Scan n values in range 0-3 and print the number of times each value has occurred
print("Scan n values in range 0-3 and print the number of times each value has occurred")
n = int(input("Enter the value of n: "))
counts = {0: 0, 1: 0, 2: 0, 3: 0}

for _ in range(n):
    value = int(input("Enter a value (0-3): "))
    if value in counts:
        counts[value] += 1

for key, value in counts.items():
    print(f"Value {key} occurred ->  {value} times.")



#Qus-2    //Create a tuple to store n numeric values and find average of all values.
print("Create a tuple to store n numeric values and find average of all values.")
n = int(input("Enter the value of n: "))
numeric_values = tuple(float(input("Enter a numeric value: ")) for _ in range(n))
average = sum(numeric_values) / n
print(f"Average of numeric values: {average}")



#Qus-3     //WAP to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output.
print("input a list of scores for N students in a list data type.")
N = int(input("Enter the number of students: "))
scores = list(map(int, input("Enter the scores separated by space: ").split()))

unique_scores = set(scores)
unique_scores.remove(max(unique_scores))
runner_up = max(unique_scores)
print("Runner-up score:", runner_up)



#Qus-4     //Create a dictionary of n persons
print("Create a dictionary of n persons")
n = int(input("Enter the number of persons: "))
persons = {}

for i in range(n):
    print(f"Details of {i+1} prson")
    name = input("Enter name: ")
    city = input("Enter city: ")
    persons[name] = city

# a) Display all names
print("Names:", list(persons.keys()))

# b) Display all city names
print("Cities:", list(persons.values()))

# c) Display student name and city of all students.
print("Name and City:")
for name, city in persons.items():
    print(f"{name}: {city}")

# d) Count number of students in each city.
from collections import Counter
city_counts = Counter(persons.values())
print("Number of students in each city:", city_counts)



#Qus-5     //Store details of n movies in a dictionary by taking input from the user.
print("Store details of n movies in a dictionary by taking input from the user.")
n = int(input("Enter the number of movies: "))
movies = []

for _ in range(n):
    name = input("Enter movie name: ")
    year = int(input("Enter release year: "))
    director = input("Enter director name: ")
    production_cost = float(input("Enter production cost: "))
    collection = float(input("Enter collection made: "))
    
    movies.append({
        'name': name,
        'year': year,
        'director': director,
        'production_cost': production_cost,
        'collection': collection
    })

# a) print all movie details
print("All Movie Details:")
for movie in movies:
    print(movie)

# b) display name of movies released before 2015
print("Movies released before 2015:")
for movie in movies:
    if movie['year'] < 2015:
        print(movie['name'])

# c) print movies that made a profit.
print("Movies that made a profit:")
for movie in movies:
    if movie['collection'] > movie['production_cost']:
        print(movie['name'])

# d) print movies directed by a particular director.
director_name = input("Enter director name to filter movies: ")
print(f"Movies directed by {director_name}:")
for movie in movies:
    if movie['director'] == director_name:
        print(movie['name'])  