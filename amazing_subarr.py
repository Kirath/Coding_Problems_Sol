# You are given a string S, and you have to find all the amazing substrings of S.
# Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

def solve(A):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    i, j = 0, 0
    res = 0
    while i < len(A):
        if A[i] in vowels:
            res += len(A) - i
        i += 1
    return res


print(solve('ABEC'))