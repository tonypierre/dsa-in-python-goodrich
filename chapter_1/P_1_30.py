# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.
from typing import Union


def times_divided_by_two(n: Union[float, int], counter: int = 0) -> int:

    if n < 0:
        raise ValueError("arg must be bigger than 0")

    if n < 2:
        return counter

    return times_divided_by_two(n / 2, counter + 1)


if __name__ == "__main__":
    x = int(input("give me a positive integer: "))
    print(times_divided_by_two(x))
