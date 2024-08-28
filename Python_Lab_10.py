
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


arr = np.array([[1, 2, 3], [4, 5, 6]])
total_sum = np.sum(arr)
print("Sum of all elements in the array:", total_sum)



arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

row_sums = np.sum(arr, axis=1)
col_sums = np.sum(arr, axis=0)

print("Sum of rows:", row_sums)
print("Sum of columns:", col_sums)

flattened_arr = arr.flatten()
sorted_arr = np.unique(flattened_arr)[-2]
print("Second maximum element in the array:", sorted_arr)



matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

result = np.dot(matrix1, matrix2)
print("Matrix multiplication result:")
print(result)





data = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
df = pd.DataFrame(data)

powers = df.apply(lambda x: x ** 2)
print("Powers of array values:")
print(powers)



exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
                      'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
first_three_rows = df.head(3)
print("First three rows of the data frame:")
print(first_three_rows)



# Assuming the DataFrame is already defined
df.replace(np.nan, 0, inplace=True)
print("DataFrame with missing values replaced:")
print(df)





# Example data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line plot
plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.title('Line Plot')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()

# Bar plot
labels = ['A', 'B', 'C', 'D', 'E']
values = [25, 30, 35, 40, 45]

plt.figure(figsize=(8, 5))
plt.bar(labels, values)
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Histogram
data = np.random.normal(0, 1, 1000)

plt.figure(figsize=(8, 5))
plt.hist(data, bins=30)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

