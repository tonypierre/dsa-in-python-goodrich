# The p-norm of a vector v = (v1,v2, . . . ,vn) in n-dimensional space is defined
# as
# v =
# p 
# vp
# 1 +vp
# 2 +· · ·+vp
# n .
# For the special case of p = 2, this results in the traditional Euclidean
# norm, which represents the length of the vector. For example, the Euclidean
# norm of a two-dimensional vector with coordinates (4,3) has a
# Euclidean norm of
# √
# 42+32 =
# √
# 16+9 =
# √
# 25 = 5. Give an implementation
# of a function named norm such that norm(v, p) returns the p-norm
# value of v and norm(v) returns the Euclidean norm of v. You may assume
# that v is a list of numbers.

from typing import List


def norm(v: List[float], p: int = 2) -> float:
    inside = 0.0
    for i in v:
        inside += pow(i, p)
    return pow(inside, 1 / p)


if __name__ == "__main__":
    x = filter(None, input("give ne numbers separated by space: ").split(" "))
    float_x = [float(i) for i in x]
    try:
        p = int(input("give me p: "))
        print(norm(float_x, p))
    except ValueError:
        print("invalid p. Returning with p = 2")
        print(norm(float_x))
