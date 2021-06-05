# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

from collections import deque


def maxSlidingWindow(nums, k):
    # max_heap = []
    # res = []
    # heapq.heapify(max_heap)
    # for i in range(len(nums)):
    #     # print(max_heap, res)
    #     while max_heap and max_heap[0][1] <= i - k:
    #         heapq.heappop(max_heap)
    #     heapq.heappush(max_heap, (-nums[i], i))
    #     if i >= k -1:
    #         res.append(-max_heap[0][0])
    # return res

    dq = deque()
    max_numbers = []

    for i in range(len(nums)):
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        if i >= k and dq and dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            max_numbers.append(nums[dq[0]])

    return max_numbers


print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))

