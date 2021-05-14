# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


def canJump(nums: list[int]) -> bool:
    lastInd = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= lastInd:
            lastInd = i
    return lastInd == 0