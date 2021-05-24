# Given two binary strings, return their sum (also a binary string).
# Example:
# a = "100"
# b = "11"


def addBinary(A, B):
    diff = len(A) - len(B)
    if diff > 0:
        for i in range(diff):
            B = '0' + B
    else:
        for i in range(-diff):
            A = '0' + A
    res = bin(int(A, 2) + int(B, 2))
    return res[2:]


print(addBinary('101','111'))