# Given the array of strings A,
# you need to find the longest string S which is the prefix of ALL the strings in the array.
# Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1
# and S2.
# For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc"


def longestCommonPrefix(A):
    s = ''
    min_len = 1000000000
    for i in range(len(A)):
        if len(A[i]) < min_len:
            min_len = (len(A[i]))
    j = 0
    while j < min_len:
        for i in range(len(A) - 1):
            if A[i][j] != A[i + 1][j]:
                break
        s += A[i][j]
        j += 1
    return s


print(longestCommonPrefix(["abcdefgh", "aefghijk", "abcefgh"]))