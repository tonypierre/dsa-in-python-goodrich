"""
Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function
"""

if __name__ == "__main__":
    x = int(input("give me a number for sum of squares: "))
    print(sum([i * i for i in range(x)]))
