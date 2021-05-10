# Given an n x n matrix where each of the rows and columns are sorted in ascending order,
# return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
import heapq
def kthSmallest(mat: list[list[int]], k: int) -> int:
    m, n = len(mat), len(mat[0])
    smallest = sum(mat[i][0] for i in range(m))
    seen = set()
    hp = [(smallest, [0] * m)]
    k -= 1

    while hp:
        total, idx = heapq.heappop(hp)
        if not k:
            return total

        k -= 1
        for i in range(m):
            col = idx[i]
            if col == n - 1: continue

            c_total, c_idx = total, idx[:]
            c_total -= mat[i][col]
            c_total += mat[i][col + 1]
            c_idx[i] = col + 1

            if tuple(c_idx) in seen: continue
            heapq.heappush(hp, (c_total, c_idx))
            seen.add(tuple(c_idx))

    return -1