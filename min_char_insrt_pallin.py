# Given an string A. The only operation allowed is to insert characters in the beginning of the string.
# Find how many minimum characters are needed to be inserted to make the string a palindrome string.
# Input Format
# The only argument given is string A.
# Output Format
# Return the minimum characters that are needed to be inserted to make the string a palindrome string

def solve(A):
    i, j = 0, len(A) - 1
    res = 0
    while i < j:
        s = ''
        if A[i] == A[j]:
            i += 1
            j -= 1
        else:
            if i == 0:
                res += 1
                j -= 1
            else:
                res += i
                i = 0

    return res


print(solve("ABC"))