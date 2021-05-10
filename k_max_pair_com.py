import heapq
def kMaxPair(A, B):
    k = len(A)
    A.sort(reverse=True)
    B.sort(reverse=True)
    res = []
    max_heap = []
    present = set([])
    heapq.heapify(max_heap)

    while True:
        if not max_heap:
            heapq.heappush(max_heap,(-(A[0] + B[0]), 0, 0))
        else:
            sm, i, j = heapq.heappop(max_heap)
            res.append(-sm)
            k -= 1
            if k == 0:
                break

            if j + 1 < len(B) and (i, j + 1) not in present:
                heapq.heappush(max_heap, (-(A[i] + B[j + 1]), i, j + 1))
                present.add((i, j + 1))
            if i + 1 < len(A) and (i + 1, j) not in present:
                heapq.heappush(max_heap, (-(A[i + 1] + B[j]), i + 1, j))
                present.add((i + 1, j))


    return res


print(kMaxPair([ 3, 2, 4, 2 ], [ 4, 3, 1, 2 ]))
