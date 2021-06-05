# Given two version numbers, version1 and version2, compare them.
# Version numbers consist of one or more revisions joined by a dot '.'.
# Each revision consists of digits and may contain leading zeros.
# Every revision contains at least one character. Revisions are
# 0-indexed from left to right, with the leftmost revision being
# revision 0, the next revision being revision 1, and so on.
# For example 2.5.33 and 0.1 are valid version numbers.
# To compare version numbers, compare their revisions in left-to-right order.
# Revisions are compared using their integer value ignoring any leading zeros.
# This means that revisions 1 and 001 are considered equal. If a version number
# does not specify a revision at an index, then treat the revision as 0. F
# or example, version 1.0 is less than version 1.1 because their revision
# 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.
# Return the following:
# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.

# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".


def compareVersion(A, B):
    v1 = list(A.split('.'))
    v2 = list(B.split('.'))
    diff = len(v1) - len(v2)
    for k in range(abs(diff)):
        if diff > 0:
            v2.append('0')
        else:
            v1.append('0')

    i, j = 0, 0
    while i < len(v1) and j < len(v2):
        if int(v1[i]) > int(v2[j]):
            return 1

        if int(v1[i]) < int(v2[j]):
            return -1

        i += 1
        j += 1
    return 0


print(compareVersion("1.01", "1.001"))