# Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.


def all_possible_permutations(var: list, counter: int) -> None:
    if len(var) == counter:
        print("".join(var))
        return None

    for i in range(counter, len(var)):
        var2 = var
        var2[i], var2[counter] = var2[counter], var2[i]
        all_possible_permutations(var2, counter + 1)


all_possible_permutations(["c", "a", "t", "d", "o", "g"], 0)
