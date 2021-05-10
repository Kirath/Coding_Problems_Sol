import heapq


def maximumScore(a, b, c):
    max_heap = []
    t, m1, m2 = 0, 0, 0
    heapq.heapify(max_heap)
    heapq.heappush(max_heap, -a)
    heapq.heappush(max_heap, -b)
    heapq.heappush(max_heap, -c)
    print(max_heap)

    while max_heap.count(0) <= 1:
        m1 = heapq.heappop(max_heap)
        m2 = heapq.heappop(max_heap)
        t += 1
        m1 += 1
        m2 += 1
        heapq.heappush(max_heap, m1)
        heapq.heappush(max_heap, m2)
        print(max_heap)

    return t

print(maximumScore(2, 4, 6))