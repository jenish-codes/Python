
# Adding Multidimensional Array

a = [[2,3],[4,5]]
b= [[1,3],[2,7]]

for i in range(0,2):
    for j in range(0,2):
        print(a[i][j]+b[i][j], end=' ')
    print()


#Declaring Multidimensional Array using index
c= [[1,3],[2,7]]
c[0][0] = 5
c[0][1] = 5
c[1][0] = 5
c[1][1] = 5
print(c)
