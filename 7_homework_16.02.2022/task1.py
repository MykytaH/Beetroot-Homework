a = float(input("Enter A value: "))
b = float(input("Enter B value: "))
while float(a) != int(a) or float(b) != int(b):
    if float(a) != int(a):
        a = input("Enter int A value, please: ")
    if float(b) != int(b):
        b = input("Enter int B value, please: ")
if a == b:
    print(f"The largest common divisor: {a}")


def eucledian_gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
            if a == b:
                return a
        elif a < b:
            b = b - a
            if a == b:
                return a


print(f"The largest common divisor: {eucledian_gcd(int(a), int(b))}")
