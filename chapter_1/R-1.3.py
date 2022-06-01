from typing import List, Tuple


def minmax(data: List[float]) -> Tuple[float, ...]:
    min = data[0]
    max = data[0]

    for idx, val in enumerate(data):
        if val >= max:
            max = val

        if val <= min:
            min = val

    return min, max


if __name__ == "__main__":
    string_input = input("Input numbers separated by space: ").split(" ")
    data = [float(i) for i in string_input]
    print(minmax(data))
