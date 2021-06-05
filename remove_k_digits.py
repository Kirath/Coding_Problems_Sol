# Given string num representing a non-negative integer num, and an integer k,
# return the smallest possible integer after removing k digits from num.
# Example 1:
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

def removeKdigits(self, num: str, k: int) -> str:
    stack = []

    for i in range(len(num)):
        # print(num[i],stack, k)
        while stack and int(stack[-1]) > int(num[i]) and k > 0:
            stack.pop()
            k -= 1
        if stack or num[i] != '0':
            # print(num[i])
            stack.append(num[i])
    # print(stack)

    while stack and k > 0:
        stack.pop()
        k -= 1
    if len(stack) == 0:
        return '0'
    else:
        return ''.join(stack)


print(removeKdigits("1432219", 3))