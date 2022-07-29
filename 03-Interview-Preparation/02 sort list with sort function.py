
list1 = [6,3,7,1,3]

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
            print(list1)
print(list1)





a = [2,1,4,3,6,9,16]


for i in range(len(a)):
    for j in range(i+1, len(a)):
        pass
