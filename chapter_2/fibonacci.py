def fibonacchi(n):
    """
    return n fibonacci sequence
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacchi(n - 2) + fibonacchi(n - 1)


print(fibonacchi(3))
