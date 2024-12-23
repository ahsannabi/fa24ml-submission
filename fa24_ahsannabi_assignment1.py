# -*- coding: utf-8 -*-
"""
Assignment 1
Machine Learning FA24
Author: Ahsan Nabi Khan

"""

#1.1. Creaye a list: nums = [3, 5, 7, 8, 12], make another list named ‘cubes’
# and append the cubes of the given list ‘nums’ 
# in this list and print it.

nums = [3,5,7,8,12]

cubes = [pow(x,3) for x in nums]

print(cubes)

#1.2. Create an empty dictionary: dict = {}, add the following data 
#to the dictionary: ‘parrot’: 2, ‘goat’: 4, ‘spider’: 8, ‘crab’: 
#10 as key value pairs.

dict = {}
dict['parrot'] = 2; dict['goat'] = 4; dict['spider'] = 8; dict['crab']=10;

#1.3. Use the ‘items’ method to loop over the dictionary (dict) and 
#print the animals and their corresponding legs. Sum 
#the legs of each animal, and print the total at the end.
sum = 0
for item in dict:
    print("Animal:",item); print("legs:",dict[item])
    sum=sum+dict[item]
print("Total:",sum)

#1.4. Create a tuple: A = (3, 9, 4, [5, 6]), 
#change the value in the list from ‘5’ to ‘8’

A = (3,9,4, [5, 6])
print("Original tuple:", A)
A[3][0] = 8
print("Modified Tuple:", A)

#1.5. Delete the tuple A.
del A;

#1.6. Create another tuple: B = (‘a’, ‘p’, ‘p’, ‘l’, ‘e’), 
#print the number of occurrences of ‘p’ in the tuple.

B = ('a', 'p', 'p', 'l', 'e')
print(B.count('p'))

#1.7. Print the index of ‘l’ in the tuple.
print(B.index('l'))

import numpy as np
'''
A =
1 2 3 4
5 6 7 8
9 10 11 12
z = np.array([1, 0, 1])
'''
#2.1 Convert matrix A into numpy array

A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(A)
z = np.array([1, 0, 1])

#2.2 Use slicing to pull out the subarray consisting of 
#the first 2 rows and columns 1 and 2. Store it in b which is a numpy 
#array of shape (2, 2).

b = A[:2, 1:3]
print(b);

#2.3 Create an empty matrix ‘C’ with the same shape as ‘A’.
C = np.empty_like(A)
print(C);

#2.4 Add the vector z to each column of the matrix ‘A’
# with an explicit loop and store it in ‘C’.
for i in range(A.shape[1]):
    C[:,i] = A[:,i] + z
    
print(C)

#Create the following:
X = np.array([[1,2],[3,4]])
Y = np.array([[5,6],[7,8]])
V = np.array([9,10])

#2.5 Add and print the matrices X and Y.
Z = X+Y
print(X)
print(Y)
print(Z)
#2.6 Multiply and print the matrices X and Y.
Z=np.dot(X,Y)
print(Z)

#2.8 Compute and print the dot product of the matrix X and vector v.
Y_sqrt = np.sqrt(Y)
print(Y_sqrt)

#2.9 Compute and print the sum of each column of X.
column_sums = np.sum(X, axis=0)
print(column_sums);

#3.1 Create a function ‘Compute’ that takes two arguments, 
#distance and time, and use it to calculate velocity.

def ComputeVelocity(distance, time):
    velocity = distance / time
    return velocity

distance = 100
time = 10
print("Velocity = distance/time = ", ComputeVelocity(distance, time))

#3.2 Make a list named ‘even_num’ that contains all even numbers up 
#till 12. Create a function ‘mult’ that takes the list
#‘even_num’ as an argument and calculates the products
# of all entries using a for loop.

even_num = [2*x+2 for x in range(int(12/2))]
def mult(even_num):
    prod_even_num = 1
    for en in even_num:
        prod_even_num*=en
    return prod_even_num

print("Product of even numbers 2 upto 12", mult(even_num))

#Task 4: Pandas
#Create a Pandas dataframe named ‘pd’ that contains 
#5 rows and 4 columns, similar to the one given below:
#C1 C2 C3 C4
#1 6 7 7
#2 7 9 5
#3 5 8 2
#5 4 6 8
#5 8 5 8

import pandas as pd
data = {
        'C1': [1,2,3,5,5],
        'C2': [6,7,5,4,8],
        'C3': [7,9,8,6,5],
        'C4': [7,5,2,8,8]
        }

pd_df = pd.DataFrame(data)

#4.1 Print only the first two rows of the dataframe.
print(pd_df.head(2))

#4.2 Print the second column.
print(pd_df['C2'])

#4.3 Change the name of the third column from ‘C3’ to ‘B3’.
pd_df.rename(columns={"C3": "B3"}, inplace=True)

#4.4 Add a new column to the dataframe and name it ‘Sum’.
pd_df['Sum'] = 0

#4.5 Sum the entries of each row and add the result in the column ‘Sum’
pd_df['Sum'] = pd_df.sum(axis=1);

print(pd_df)

#4.6 Read CSV file named ‘hello_sample.csv’ 
#(the file is available in the class Google Drive shared folder) 
#into a Pandas dataframe.

import os 
cwd = os.getcwd()
df = pd.read_csv(cwd+'/Downloads/Comsats PhD/FA24ML/hello_sample.csv')

#4.7 Print complete dataframe.
print(df)

#4.8 Print only bottom 2 records of the dataframe.
print(df.tail(2))

#4.9 Print information about the dataframe.
print(df.info())

#4.10 Print shape (rows x columns) of the dataframe.
print(f"Shape of the dataframe: {df.shape}")

#4.11 Sort the data of the dataFrame using column ‘Weight’.
df_sorted = df.sort_values(by='Weight')
print(df_sorted)

#4.12 Use isnull() and dropna() methods of the 
#Pandas dataframe and see if they produce any changes.

print("Null values in the dataframe:")
print(df.isnull())
df_dropped = df.dropna()
print("\nDataFrame after dropping null values (if any):")
print(df_dropped)