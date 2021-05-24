# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 1 is read off as one 1 or 11.
# 11 is read off as two 1s or 21.
# 21 is read off as one 2, then one 1 or 1211.
# Given an integer n, generate the nth sequence.
# Note: The sequence of integers will be represented as a string.
# Example:
# if n = 2,
# the sequence is 11.

def countAndSay(A):
    if A == 1:
        return '1'
    if A == 2:
        return '11'
    s = '11'
    for i in range(3, A + 1):
        ans = ''
        s += '@'
        cnt = 1
        for j in range(0, len(s) - 1):
            if s[j] == s[j + 1]:
                cnt += 1
            else:
                ans += str(cnt) + s[j]
                cnt = 1
                # print(ans)
        s = ans
    return s


print(countAndSay(4))