# Given an n x n matrix where each of the rows and columns are sorted in ascending order,
# return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
import heapq


def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
    min_heap = []
    res = []
    heapq.heapify(min_heap)
    present = set([])
    heapq.heapify(min_heap)
    while True:
        if not min_heap:
            heapq.heappush(min_heap, ((matrix[0][0]), 0, 0))
        else:
            sm, i, j = heapq.heappop(min_heap)
            res.append(sm)
            k -= 1
            if k == 0:
                break

            if j + 1 < len(matrix[i]) and (i, j + 1) not in present:
                heapq.heappush(min_heap, ((matrix[i][j + 1]), i, j + 1))
                present.add((i, j + 1))
            if i + 1 < len(matrix) and (i + 1, j) not in present:
                heapq.heappush(min_heap, ((matrix[i + 1][j]), i + 1, j))
                present.add((i + 1, j))
    return res[-1]