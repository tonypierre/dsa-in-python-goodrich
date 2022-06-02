from random import choices


def test_birthday_paradox(students: int, iterations: int):
    true_cases = 0
    count = 0
    while count < iterations:
        population = range(1, 366)
        samples = choices(population, k=students)
        if len(set(samples)) < students:
            true_cases += 1

        count += 1

    return true_cases / iterations


if __name__ == "__main__":
    # x = input("students, iterations: ").split(" ")
    print(f"{test_birthday_paradox(100, 1000000) * 100} percent")
