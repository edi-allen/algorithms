#!/usr/bin/python3
import string
"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
"""

def solve(encoded):
    letters = { x+1:y for (x,y) in enumerate(string.ascii_lowercase)}
    messages = []
    def decode(encoded, message=''):
        for index in range(len(encoded)):
            left = encoded[0:index+1]
            if int(left) in letters:
                letter = letters[int(left)]
                right = encoded[index+1:]
                if len(right) > 0:
                    decode(right, message + letter)
                else:
                    messages.append(message+letter)
    decode(encoded, '')
    print(messages)
    print(len(messages))


if __name__ == '__main__':
    solve('111')
