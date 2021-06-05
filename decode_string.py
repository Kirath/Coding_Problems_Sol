# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string
# inside the square brackets is being repeated exactly k times.
# Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain
# any digits and that digits are only for those repeat numbers,
# k. For example, there won't be input like 3a or 2[4].

from collections import deque


def decodeString(s):
    res = ''
    str_stack = deque()
    count_stack = deque()
    ind = 0
    while ind < len(s):
        if s[ind].isnumeric():
            c = 0
            while s[ind].isnumeric():
                c = 10 * c + (int(s[ind]) - 0)
                ind += 1
            count_stack.append(c)

        elif s[ind] == '[':
            str_stack.append(res)
            res = ''
            ind += 1

        elif s[ind] == ']':
            temp = []
            cnt = count_stack.pop()
            temp.append(str_stack.pop())
            for i in range(cnt):
                temp.append(res)
            res = ''.join(temp)
            ind += 1

        else:
            res += s[ind]
            ind += 1
    return res


print(decodeString("3[a]2[bc]"))