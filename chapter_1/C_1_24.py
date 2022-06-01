# Write a short Python function that counts the number of vowels in a given
# character string.


def count_vowels(string: str) -> int:
    vowels: set = {"a", "e", "i", "o", "u"}
    count = 0
    for i in string:
        if i in vowels:
            count += 1

    return count


if __name__ == "__main__":
    x: str = input("give me a string: ")
    print(count_vowels(x))
