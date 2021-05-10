# Problem Description
# Given N bags, each bag contains Bi chocolates. There is a kid and a magician.
# In one unit of time, kid chooses a random bag i, eats Bi chocolates,
# then the magician fills the ith bag with floor(Bi/2) chocolates.
# Find the maximum number of chocolates that kid can eat in A units of time.
import heapq
def nchoc(self, A, B):
    res = 0
    temp = 0
    max_heap = [-x for x in B]

    heapq.heapify(max_heap)
    for i in range(A):
        if max_heap:
            temp = -heapq.heappop(max_heap)
            res += temp
            if temp // 2 != 0:
                temp //= 2
                heapq.heappush(max_heap, -temp)
    return res % (10 ** 9 + 7)