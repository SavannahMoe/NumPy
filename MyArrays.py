import random
import numpy as np


integers = np.array([x for x in range(2, 21, 2)])
print(integers)

integers = np.array([[1, 2, 3], [4, 5, 6]])
print(integers)

floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
print(floats)

a = integers.dtype
b = integers.ndim  # number of demensions
c = integers.shape  # tuple that returns the deminsions of the array
d = integers.size  # total elements in the array

print()


for row in integers:
    print(type.row)
    print(row)
    for col in row:
        print(col, end=" ")


for i in integers.flat: #iterates through all values disregarding columns and rows
    print(i)
'''
############
##EXERCISE##
############
'''
a = np.array(
    [
        [random.randint(1,10) for x in range (5)],    #"for x in range(5) carries out the random module 5 times"
        [random.randint(1,10) for x in range (5)],
    ]
)
print(a)

b = np.array(np.random.randint(1,10, size = (2,5)))
print(b)
#creates a 2 dimensional array of 5 integers elements each using the random module
#list comprehension print out its dimension, shape, and size


c = np.zeros(5) #creates an array of 5 elements of zeros (by default float type)
print(np.ones(5))   #creates an array of 5 elements of 1s (by default float type)

print(np.ones((2,4), dtype=int))    #create an array of 2 by 4 of ones of type int

print(np.full((3,5),13)) #creates an array of 3 rows of 5 columns of the numebr 13

print(np.arange(5)) #like the range function, using integers

print(np.arange(5,10)) #indicates lower liimit but not upper limit

print(np.arange(10, 1, -2)) # third value indicates step value for descending order

print(np.linspace(0.0,1.0, num=5)) #evenly spaced flaot range 


array1 = np.arange(1,21)
array2 = array1.reshape(4,5)    #reshape method changes the deminsions, in this case from 1,20 to 4,5 ***must have the same number of elements

print(array1)
print(array2)



array3= np.arange(1, 100001).reshape(4, 25000)
print(array3)

array4 = np.arange(1,100001).reshape(100,1000)
print(array4)

numbers = np.arange(1,6)
numbers+=10
print(numbers)


###BROADCASTING###

print(numbers*2) #numbers *[2,2,2,2,2]
print(numbers**3)

#numbers is unchanged by the aritmetic operators
print(numbers)

##multiplying integer arrays with floating pt arrays(results is floating pt)
numbers2 = np.linspace(1.1, 5.5, 5)
a= numbers*numbers2
print(a)

#comparing arrays
print(numbers >= 13)

print(numbers2 < numbers)

print(numbers ==numbers2)
