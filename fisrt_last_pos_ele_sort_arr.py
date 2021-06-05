# Given an array of integers nums sorted in ascending order, find the starting and
# ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

import heapq
def searchRange(nums, target):
    min_heap = []
    heapq.heapify(min_heap)
    for i in range(len(nums)):
        heapq.heappush(min_heap, (nums[i], i))
    k, ind = 0, 'q'
    if len(nums) == 0 or target < nums[0] or target > nums[len(nums) - 1]:
        return [-1, -1]
    while min_heap:
        temp, i = heapq.heappop(min_heap)
        if temp == target:
            ind = i
            k += 1

    if ind == 'q':
        return [-1, -1]
    return [ind - k + 1, ind]


print(searchRange([5,7,7,8,8,10], 8))