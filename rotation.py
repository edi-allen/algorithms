#!/usr/bin/env python3

def rotate(array):
    if len(array) <= 1:
        return array
    last = array[-1]
    for n in reversed(range(0, len(array)-1)):
        array[n+1] = array[n]
    array[0] = last
    return array

if __name__ == '__main__':
    assert [5, 1, 2, 3, 4] == rotate([1,2,3,4,5])
