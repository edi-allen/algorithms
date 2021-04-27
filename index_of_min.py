#!/usr/bin/python3

"""
Find index of the minimun element in a list.
"""

def index_of_min(array):
    index = 0
    for i in range(1, len(array)):
        if array[i] < array[index]:
            index = i
    return index

if __name__ == '__main__':
    array = [3, 1, 0, 7, 2, 9]
    print(array)
    print(index_of_min(array))
