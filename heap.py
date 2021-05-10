import heapq

arr2 = [50, 6, 8, 9, 10]
arr3 = [-3, -2, -4, -2 ]
arr = [ -4, -3, -1, -2 ]

heapq.heapify(arr)
print(arr)
heapq.heappush(arr, 7)
heapq.heappop(arr)
print(heapq.heappushpop(arr, 2))
print(heapq.heapreplace(arr, 2))
print(heapq.nlargest(3,arr))
print(heapq.nsmallest(3, arr))
