# There is a special kind of apple tree that grows apples every day for n days.
# On the ith day, the tree grows apples[i] apples that will rot after days[i] days,
# that is on day i + days[i] the apples will be rotten and cannot be eaten.
# On some days, the apple tree does not grow any apples, which are denoted by apples[i] == 0 and days[i] == 0.
# You decided to eat at most one apple a day (to keep the doctors away).
# Note that you can keep eating after the first n days.
# Given two integer arrays days and apples of length n, return the maximum number of apples you can eat.

# Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
# Output: 7
# Explanation: You can eat 7 apples:
# - On the first day, you eat an apple that grew on the first day.
# - On the second day, you eat an apple that grew on the second day.
# - On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot.
# - On the fourth to the seventh days, you eat apples that grew on the fourth day.

import heapq

def eatenApples(apples, days):
    min_heap = []
    res = 0
    d = 1
    i = 0
    while i < len(apples) or min_heap:

        if i < len(apples):
            valid = days[i] + d
            heapq.heappush(min_heap, (valid, apples[i]))
            # print(min_heap)
            i += 1

        while min_heap and min_heap[0][0] <= d:
            heapq.heappop(min_heap)
            # print(min_heap,res)
        if min_heap:

            r_days, r_apples = heapq.heappop(min_heap)
            r_apples -= 1
            res += 1
            if r_apples > 0:
                heapq.heappush(min_heap, (r_days, r_apples))

        d += 1
        # print(res,d)

    return res


print(eatenApples([1,2,3,5,2], [3,2,1,4,2]))