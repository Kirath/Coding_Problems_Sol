#Given an array s.t. two numbers are non repeating.
# Find the numbers


def find_numbers(arr):
    xor_p, temp = 0, 0
    for i in range(len(arr)):
        xor_p ^= arr[i]
    # print(xor_p)
    for j in range(32):
        if xor_p & (1 << j) != 0:
            temp = xor_p & (1 << j)
            break
    # print(temp)
    xor_0, xor_1 = 0, 0
    for k in range(len(arr)):
        if arr[k] & temp == 0:
            xor_0 ^= arr[k]
            # print(xor_0)
        else:
            xor_1 ^= arr[k]
    return xor_0, xor_1


arr = list(map(int,input().split()))
print(find_numbers(arr))
