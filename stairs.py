#!/usr/bin/python3


def solve(valid_steps, taken, remaining):
    for valid_step in valid_steps:
        if (remaining - valid_step) > 0:
            solve(valid_steps, taken + [valid_step], remaining - valid_step)
        elif (remaining - valid_step) == 0:
            print(taken + [valid_step])


if __name__ == '__main__':
    valid_steps = [1, 4]
    n = 4
    solve(valid_steps, [], n)
