import numpy as np

# Create arrays using numpy library and leverage list
# Create single dimension arrays using arange function
# Create arrays and initialize with prefixed values such as 0s and 1s
# Create evenly spaced samples using linespace
# Create Identity Matrix
# Reshape an existing array to other dimension

#Create lists of lists and print output
mylist = [1,2,3]
print("List values: ", mylist)
print("data type of list: ", type(mylist))
array = np.array(mylist)
print("array values: ", array)
print("data type of array: ", type(array))


print("####################################################################")
print("Matrix")
# matrixes
mymat = [[1,2,3],[4,5,6],[7,8,9]]
print("My matrix: ", mymat)
# convert the embedded lists to array using np.array function.. the output should have 3 rows and 3 col
print("The matrix after conversion...", np.array(mymat))

print("####################################################################")
print("start stop in arange")
# arange function is similar to range function in python, you can specify(start, stop, increment) in range function
startStopNoIncre = np.arange(0,10)
print("this one has no increment and stops before 10..", startStopNoIncre)
startStopWithIncre = np.arange(0, 10, 2)
print("this one has increment...", startStopWithIncre)

print("####################################################################")
print("Init array with 0s")
# Generate arrays with 0s initialized
print(np.zeros(3))
print(np.zeros((3,4))) # this gives a matrix of 3 row 4 col

print("####################################################################")
print("Init array with 1s")
# Generate arrays with 1s init
print(np.ones((2,2))) # this gives matrix of 2 row 2 col

print("####################################################################")
print("Linspace")
# Linspace function - returns evenly spaced numbers over a specified interval, calculated over the interval [start, stop].
# This returns 20 samples in the range 0-10
print(np.linspace(0, 10, 20))

print("####################################################################")
print("Identity Matrix")
# Create an identity matrix - a square matrix with ones on the main diagonal.
# Square matrix - number of rows equal number of col
print(np.eye(3))

print("####################################################################")
print("Randomizing array")
# Can create random matrix using np.random
print(np.random.rand(5,5))

print("####################################################################")
print("Reshape array")
# it is common to reshape a 1D array to 2D array
initArray = np.arange(0,10)
print(initArray.reshape(5,2))

#useful functions to find max and min of array.. array.max() and array.min()

#PART 2
# Performing operations on Array with Array
# Performing operations on Array with Scalar
# Universal Array functions
print("####################################################################")
print("Array on Array")
array1 = np.arange(0,11)
array2 = np.arange(0,11)
print("Array sum... ", array1 + array2)
print("Array diff...", array1 - array2)
print("Array mul...", array1 * array2)

print("####################################################################")
print("Array on Scalar")
print("Array1 + 10 ", array1 + 10)
print("Array1 ** 2 ", array1 ** 2)

print("####################################################################")
print("Universally important functions")
print("Sq root: ", np.sqrt(array1))
print("max value: ", np.max(array1))
print("min value: ", np.min(array1))
print("sin value: ", np.sin(array1))
print("cosine value: ", np.cos(array1))

#Array attributes - ndim, shape, size, dtype
print("Array1 dimension: ", array1.ndim)
print("Array1 shape: ", array1.shape)
print("Array1 size: ", array1.size)
print("Array1 dtype: ", array1.dtype)

print("####################################################################")
#Accessing elements in matrix using indexes
matrix1 = np.array([[1,2,3,4,5],[10,23,30,32,50]])
print("first row elements of matrix1: ", matrix1[0])
print("second row of elements: ", matrix1[1])
print("first col of matrix1: ", matrix1[:,1])
print("first and second col elements of matrix1: ", matrix1[:,0:2])
print("first and forth col elements of matrix1: ", matrix1[:, :4])
print("second row elemnts of matrix1: ", matrix1[1,1:3])

# Flaten 2d array
print("####################################################################")
mainArr = np.array([[10,23,33], [2,1,3]])
print("flatten array: ", np.ravel(mainArr))