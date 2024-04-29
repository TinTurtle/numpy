x = int(input())
y = int(input())
z = int(input())
n = int(input())

L = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            l = [i,j,k]
            if((x+y+z) != n):
                L.append(l)

print(L)