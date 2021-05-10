import heapq


def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
    min_heap = []
    heapq.heapify(min_heap)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            heapq.heappush(min_heap, matrix[i][j])
    res = heapq.nsmallest(k, min_heap)
    return res[k - 1]
