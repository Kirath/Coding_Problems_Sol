# Given an 1D integer array A of size N you have to find and return the
# B largest elements of the array A.
# NOTE:
# Return the largest B elements in any order you like.
# Input 1:
import heapq


def solve(A, B):
    max_heap = []
    res = []
    heapq.heapify(max_heap)
    for i in A:
        heapq.heappush(max_heap, -i)
    while B > 0:
        res.append(-heapq.heappop(max_heap))
        B -= 1
    return res


A = [11, 3, 4]
B = 2
print(solve(A,B))