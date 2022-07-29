# find largest num

arr1 = [1,8,7,56,90]
n= len(arr1)

def largest(arr,n):
    largestnum = arr[0]
    for i in range(n):
        if arr[i] >= largestnum:
            largestnum = arr[i]
    print(largestnum)

largest(arr1, n)


