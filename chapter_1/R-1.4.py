"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""
# from typing import List


def sum_of_squares(n: int) -> int:
    if n < 0:
        raise ValueError("the input number has to be bigger than 0")

    if n == 0:
        0

    count = 0
    val = 0
    while count < n:
        val += count**2
        count += 1
    return val


if __name__ == "__main__":
    x = int(input("Give me a number: "))
    print(sum_of_squares(x))
