

arr = [1,9,8,2,7]
n = len(arr)

def rearrangeArray(arr, n):
    arr.sort()
    tempArr = [0] * (n+1)
    print(tempArr)
    ArrIndex = 0

    i = 0
    j = n-1

    while(i<=n // 2 or j > n//2):
        tempArr[ArrIndex] = arr[i]
        ArrIndex = ArrIndex + 1
        tempArr[ArrIndex] = arr[j]
        ArrIndex = ArrIndex + 1
        i = i + 1
        j = j - 1

    for i in range(0,n):
        arr[i] = tempArr[i]
        print(arr[i], end= ' ')

rearrangeArray(arr, n)






'''
for i in range(0, n):
    print(arr[i], end= ' ')
'''
