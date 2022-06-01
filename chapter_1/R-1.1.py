def is_mutiple(n: int, m: int) -> bool:
    return False if n % m else True


n, m = input("Input Two Numbers:  ").split(" ")

print(is_mutiple(int(n), int(m)))
