# def printName():
#     print("Akhmadjon")
#
#
# printName()
import math


# def fancy_hello_world():
#     fancy_string = """
#     ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
#     ───█▒▒░░░░░░░░░▒▒█───
#     ────█░░█░░░░░█░░█────
#     ─▄▄──█░░░▀█▀░░░█──▄▄─
#     █░░█─▀▄░░░░░░░▄▀─█░░█
#     """
#     return fancy_string

# print(fancy_hello_world());
#
# def area(radius):
#     a = math.pi * radius**2
# def absolute_value(x):
#     if x < 0:
#         return -x
#     elif x > 0:
#         return x
#     elif x==0:
#         return 0

def absolute_value(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1

print(absolute_value(0, 1))

# task 5

def test_is_valid(test):
    if(isinstance(test, int)==True) and (1 <= test <=3):
        return True
    else:
        return False

print(test_is_valid("3"))
print(test_is_valid(2))
print(test_is_valid(1))
