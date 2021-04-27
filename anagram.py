#!/usr/bin/env python3

def is_anagram(str1, str2):
    s1 = ''.join(sorted(str1))
    s2 = ''.join(sorted(str2))
    return s1 == s2

if __name__ == '__main__':
    assert is_anagram('cinema', 'iceman')
