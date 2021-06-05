# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you
# like (i.e., buy one and sell one share of the stock multiple times).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must
# sell the stock before you buy again).

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

from collections import deque

def maxProfit(prices):
    stack = deque()
    profit = 0
    for i in range(len(prices) - 1):
        stack.append(prices[i])
        if stack and prices[i + 1] < stack[-1]:
            stack.pop()
            stack.append(prices[i + 1])
        elif stack and prices[i + 1] > stack[-1]:
            temp = stack.pop()
            profit += prices[i + 1] - temp
    return profit


print(maxProfit( [7,1,5,3,6,4]))
