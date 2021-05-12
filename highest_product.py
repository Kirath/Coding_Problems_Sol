# Given an array A, of N integers A.
# Return the highest product possible by multiplying 3 numbers from the array.
# NOTE: Solution will fit in a 32-bit signed integer.


# @param A : list of integers
# @return an integer
def maxp3(A):
    if len(A)<3:
        return 0
    A.sort()
    return max(A[-1]*A[-2]*A[-3],A[0]*A[1]*A[-1])