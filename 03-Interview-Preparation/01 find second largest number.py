


list1 = [10,38,90,100]

def findLargest(num):
    largest = num[0]
    secondlargest = num[0]

    for i in range(len(num)):
        if num[i] > largest:
            largest = num[i]

    for i in range(len(num)):
        if num[i] > secondlargest and num[i] != largest:
            secondlargest = num[i]
    return secondlargest

print(findLargest(list1))





'''


def findLargest(arr):
    secondLargest = arr[0]
    largest = arr[0]

    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    for i in range(len(arr)):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    return secondLargest

print(findLargest([10,20,4,45,99]))
'''
