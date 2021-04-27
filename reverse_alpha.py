#!/usr/bin/env python3
import string

def reverse_alpha(s):
    s = list(s)
    alphabet = set(string.ascii_lowercase)
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] in alphabet and s[right] in alphabet:
            swap(s, left, right)
            left = left + 1
            right = right - 1
        elif s[left] in alphabet and s[right] not in alphabet:
            right = right - 1
        elif s[left] not in alphabet and s[right] in alphabet:
            left = left + 1
        else:
            left = left + 1
            right = right - 1
    
    return ''.join(s)

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

if __name__ == '__main__':
    s = 'sea!$hells3'
    assert reverse_alpha(s) == 'sll!$ehaes3'
