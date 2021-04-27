#!/usr/bin/python3

def solve(numbers, k):
    size = len(numbers)
    for i in range(size - 1):
        for j in range(i+1, size):
            if numbers[i] + numbers[j] == k:
                return True
    return False


def solve_with_set(numbers, k):
    s = set(numbers)
    for n in numbers:
        m = k - n
        if m != n and m in s:
            return True
    
    return False


if __name__ == '__main__':
    numbers = [10, 15, 3, 7, 10] 
    k = 25
    #print(solve(numbers, k)) 
    print(solve_with_set(numbers, k)) 
