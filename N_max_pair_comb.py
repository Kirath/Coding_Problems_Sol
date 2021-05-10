import heapq


def maxPair(A, B):
    min_heap = []
    heapq.heapify(min_heap)
    A.sort()
    B.sort()
    n = len(A)

    for i in range(n - 1, -1, -1):
        a = A[i]
        # state of heap before any element was inserted
        pr_heap = min_heap[:]

        for j in range(n - 1, -1, -1):
            b = B[j]
            pair_sum = a + b
            heapq.heappush(min_heap, pair_sum)
            # To check solution set is exceeding the requirement(let's say = 4)
            if len(min_heap) > n:
                x = heapq.heappop(min_heap)
                # --
                if x == pair_sum:
                    break

        if pr_heap == min_heap:
            break

    return sorted(min_heap)[::-1]


print(maxPair([ 3, 2, 4, 2 ], [ 4, 3, 1, 2 ]))