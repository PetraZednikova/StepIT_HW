#task 1

""" find the greatest common divisor of two integers"""
a = int(input("Select first number: "))
b = int(input("Select second number: "))


def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

print(f"The greates common integer for numbers {a} and {b} is {greatest_common_divisor(a, b)}.")






