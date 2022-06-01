# Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.

from typing import List


def reverse_list(data: List) -> None:
    i = 0
    j = len(data) - 1

    while i < j:
        data[i], data[j] = data[j], data[i]
        i += 1
        j -= 1

    print(data)


if __name__ == "__main__":
    x = input("input values separated by space").split(" ")
    reverse_list(x)
