import numpy as np
# Python program for
# Creation of Arrays
 
# Creating an Array from list
arr = np.array([1, 2, 3])
print("Array created using passed list:\n",arr)
 
# Creating an array from tuple
print("\nArray created using passed tuple:\n", arr)

arr = np.array([[1,2,3],[4,5,6]])

print("\nDimension : ",arr.ndim)

print("Size of Elements : ",arr.itemsize)

print("Datatype of elements : ",arr.dtype)

print("No. of Elements : ",arr.size)

print("Shape :",arr.shape)