# N light bulbs are connected by a wire.
# Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb.
# Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.
# You can press the same switch multiple times.
# Note : 0 represents the bulb is off and 1 represents the bulb is on.

# @param A : list of integers
# @return an integer
def bulbs(A):
    c = 0
    for i in range(len(A)):
        if A[i] == 0 and c % 2 == 0:
            c += 1

        if A[i] == 0 and c % 2 != 0:
            continue

        if A[i] == 1 and c % 2 == 0:
            continue

        if A[i] == 1 and c % 2 != 0:
            c += 1
    return c