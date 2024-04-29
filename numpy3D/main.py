import numpy as np

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(arr)

print(arr[1][0][2])

for i in range(0,2):
    for j in range(0,2):
        for k in range(0,3):
            print(arr[i][j][k])
