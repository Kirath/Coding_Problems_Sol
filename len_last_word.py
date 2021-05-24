# Given a string s consists of upper/lower-case alphabets and
# empty space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.
# Note: A word is defined as a character sequence consists of non-space characters only.

def lengthOfLastWord(A):
    words = list(A.split())
    if len(words) > 0:
        # print(words)
        return len(words[len(words) - 1])
    return 0


print(lengthOfLastWord("Hello World"))