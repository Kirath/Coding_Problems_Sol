# Compare two version numbers version1 and version2.
# If version1 > version2 return 1,
# If version1 < version2 return -1,
# otherwise return 0.
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth
# second-level revision of the second first-level revision.


def compareVersion(A, B):
    v1 = list(A.split('.'))
    v2 = list(B.split('.'))
    if v1[0] == v2[0]:
        if len(v1) > len(v2):
            if int(v1[len(v1) - 1]) != 0:
                return 1
            else:
                return 0
        if len(v1) < len(v2):
            if int(v2[len(v2) - 1]) != 0:
                return -1
            else:
                return 0

    i, j = 0, 0
    while i < len(v1) and j < len(v2):
        if int(v1[i]) > int(v2[j]):
            return 1

        if int(v1[i]) < int(v2[j]):
            return -1

        i += 1
        j += 1
    return 0