# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by
# deleting some (can be none) of the characters without disturbing the relative
# positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Input: s = "abc", t = "ahbgdc"
# Output: true

def isSubsequence(s, t):
    i, j = 0, 0

    while j < len(t) and i < len(s):
        if s[i] == t[j]:
            j = j + 1
            i += 1
        else:
            j += 1
    if i <= len(s) - 1:
        return False
    return True


print(isSubsequence("abc", "ahbgdc"))