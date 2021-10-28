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
