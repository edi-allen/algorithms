#!/usr/bin/python3

def binarysearch(array, n):
    return helper(array, n, 0, len(array) - 1) 


def helper(array, n, j, k):
    print(j, k)
    if k < j:
        return -1
    middle = (k + j) // 2
    if array[middle] < n:
        return helper(array, n, middle + 1, k)
    elif array[middle] > n:
        return helper(array, n, j, middle - 1)
    else:
        return middle


if __name__ == '__main__':
    numbers = [1, 5, 2, 9, 25, 4, 33]
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)
    print(binarysearch(sorted_numbers, 25))
