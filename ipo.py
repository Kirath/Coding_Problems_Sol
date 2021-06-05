# Suppose LeetCode will start its IPO soon. In order to sell a good price of
# its shares to Venture Capital, LeetCode would like to work on some
# projects to increase its capital before the IPO. Since it has limited resources,
# it can only finish at most k distinct projects before the IPO. Help LeetCode design
# the best way to maximize its total capital after finishing at most k distinct projects.
# You are given n projects where the ith project has a pure profit profits[i] and
# a minimum capital of capital[i] is needed to start it.
# Initially, you have w capital. When you finish a project, you will obtain its pure
# profit and the profit will be added to your total capital.
# Pick a list of at most k distinct projects from given projects to maximize your final capital,
# and return the final maximized capital.
# The answer is guaranteed to fit in a 32-bit signed integer.

from heapq import heappush, heapify, heappop

def findMaximizedCapital(k, w, Profits, Capital):
    heap_1 = [[-profit, capital] for profit, capital in zip(Profits, Capital)]
    heap_2 = []
    heapify(heap_1)

    while heap_1 and k:
        if heap_1[0][-1] <= w:
            profit, capital = heappop(heap_1)
            w += -profit
            k -= 1
        else:
            profit, capital = heappop(heap_1)
            heappush(heap_2, [capital, profit])
        while heap_2 and heap_2[0][0] <= w:
            capital, profit = heappop(heap_2)
            heappush(heap_1, [profit, capital])
    return w


print(findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))