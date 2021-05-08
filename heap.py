import heapq

arr = [50, 6, 8, 9, 10]
heapq.heapify(arr)
heapq.heappush(arr, 7)
heapq.heappop(arr)
print(heapq.heappushpop(arr, 2))
print(heapq.heapreplace(arr, 2))
print(heapq.nlargest(3,arr))
print(heapq.nsmallest(3, arr))
