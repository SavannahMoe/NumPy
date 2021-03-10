import numpy as np
'''
grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

##ROWS represent grades for each student 
##Columns - represent grades for each tests

a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

g = grades.mean(axis = 0) #finding and returning the mean by test (avg of 1st, 2nd, and 3rd test)
print("Average of each test:", g)

h = grades.mean(axis = 1)
print("Average of each student:", h)

numbers = np.array([1,4,9,16,25,36])
sqrt = np.sqrt(numbers)
print(sqrt)

numbers2 = np.arange(1,7)*10
print(numbers2)

add = np.add(numbers,numbers2)
print(add)

multiply= np.multiply(numbers2, 5)
print(multiply)

numbers3 = numbers2.reshape(2,3)
print(numbers3)

numbers4 = np.array([2,4,6])

multiply2 = np.multiply(numbers3,numbers4)
print(multiply2)  #this works because numebrs 4 has the same length as each row of numbers3 so NumPy can apple the 
                    #multiply operation by treating numbers4 as if it were the following array

#Indexing and Slicing
#if you use colon: it is consecutive, if you use comma it is specific no consecutive
grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

a = grades[0,1]
print(a) #output= 96

b = grades[1]
#array([100,87,90])

#to select multiple sequential rows use slice
firsttwo = grades[0:2]  #slicing and does not include upper limit
    #array ([[87,96,70]
    #        [100,87,90]])

#to selesct multiple non-sequential rows, use a list of rows indices:
grades[[1,3]]
#array([[100,87,90]
#       [100,81,82]])

#all rows and only the first column
c = grades[:,0]
print(c)

#you can select consecutive columns using slicing
d = grade[:,1:3]
#array 

#or specific colunms using a list of columns indices:
e = grades[:,[0,2]]
'''
##CLASS EXERCISE##
'''
grades = np.array(np.random.randint(60,101,12).reshape(3,4))
print(grades.mean())
print(grades.mean(axis = 0))
print(grades.mean(axis = 1))

##Shallow coppies (view) #whatever you do to view effects original array and vice versa
#the arreay method view returns a new array object with a view of the original array

numbers = np.arange(1,6)
#array([1,2,3,4,5,6])

numbers2 = numbers.view()
#array([1,2,3,4,5,6])

numbers[1]*=10
print(numbers2)
#array([1,20,3,4,5,6])

numbers2[1]/=10
print(numebers)
#array([1,2,3,4,5,6])

#Slice views
#slices also create views. lets make number 2 a slice that views only the first three elements 
number2 = numbers[0:3]

#to verify it is a veiw, lets modify an element in the original array and see the view array
numbers[1]*= 20
print(numbers2)
#array9[1,40,3]


#####Deep copies(copy)
#tha array method copy returns a new arrya obbject with a deep copy of the original array
numbers = np.arange(1,6)
numbers2 = numbers.copy()

numbers[1] *= 10 
print(numebers)
#array([1,20,3,4,5,6])
print(numbers2)
#array([1,2,3,4,5,6])

'''
###
'''the array method reshape and resize both enable you to change an array's deminsions.'''

grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

a = grades.reshape(1,6)
print(a)
#arra9[87,96,70,100,87,90]

b = grades.resize(1,6)
print(grades)

#method flatten deep copies the original array's data:
flattened = grades.flatten()

#alternatively: method ravel produces a view(shallow copy) of the original array, which shares the grades's array's data
raveled = grades.ravel()

#confirm that they share the same data
raveled[0] = 100
reveled[6] = 99
print(grades)

## since it is a view andd they shar the same data, we can look at grade


##TRANSPOSE##
# you can quickly transpose an array's rows and columns aka flip the array . so the rows become the columns and vice versa
# and the T attribute returns a transposed view (shallow copy of the array) 

transposed = grades.T
print(transposed)


#you can combine arrays be adding more columns or more rows known as horizontal stacking and vertical stacking 
#HSTACK
grades = np.array([[87,96,70],[100,87,90])
grades2 = np.array([94,77,90],[100,81,82]])

#we combine grades and grades2 with NumPy hstack
h_grades = np.hstack((grades, grades2))

print(h_grades)

print(grades)   

#VSTACK
v_grades = np.vstack((grades, grades2))
print(v_grade)