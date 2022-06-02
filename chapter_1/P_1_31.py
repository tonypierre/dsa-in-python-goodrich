# Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible.

CHANGETYPE = (100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01)


def give_change(money: float, Changes=[0 for _ in range(len(CHANGETYPE))], counter=0):
    if counter == len(CHANGETYPE):
        print(Changes)
        return None

    Changes_copy = Changes
    money_copy = money % CHANGETYPE[counter]
    Changes_copy[counter] = int(money / CHANGETYPE[counter])

    give_change(money_copy, Changes_copy, counter + 1)


if __name__ == "__main__":
    x = float(input("Money: "))
    give_change(x)
