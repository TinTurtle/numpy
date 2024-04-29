import numpy as np

#Normal Decalaration
#Datatype is guessed by python
arr = np.array([[1,2,3],[4,5,6]])

#Forced Datatype
arr1 = np.array([[1,2,3],[4,5,6]],dtype = np.int64)

print(arr)

print("1st row 2nd column element :",arr[0][1])

for i in range(0,2):
    for j in range(0,3):
        print(arr[i][j],end=" ")
    print()