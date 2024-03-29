# You are given two integer arrays nums1 and nums2 both of unique elements,
# where nums1 is a subset of nums2.
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
# The Next Greater Number of a number x in nums1 is the first greater number to
# its right in nums2. If it does not exist, return -1 for this number.
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation:
# For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
# For number 1 in the first array, the next greater number for it in the second array is 3.
# For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
from collections import deque


def nextGreaterElement(nums1, nums2):
    hash_map = dict()
    stack = deque()
    res = []

    for num in nums2:
        while stack and stack[-1] < num:
            hash_map[stack.pop()] = num
        stack.append(num)

    for j in nums1:
        ans = hash_map.get(j)

        if ans is None:
            ans = -1
        res.append(ans)
    return res





