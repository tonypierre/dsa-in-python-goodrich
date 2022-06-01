def is_even(n: int) -> bool:
    """
    10111  -  odd
        1  -    1
    10111  -  odd
    """
    return False if n & 1 == n else True


if __name__ == "__main__":
    n = int(input("Give me a number to check even or odd"))
    print(is_even(n))
