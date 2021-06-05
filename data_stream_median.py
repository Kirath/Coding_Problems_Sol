# The median is the middle value in an ordered integer list. If the size of the list is even,
# there is no middle value and the median is the mean of the two middle values.
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far.
# Answers within 10-5 of the actual answer will be accepted.

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.max_heap = []
        self.min_heap = []
        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)

    def addNum(self, num: int) -> None:
        left_len = len(self.max_heap)
        right_len = len(self.min_heap)
        if left_len == 0:
            heapq.heappush(self.max_heap, -num)
        elif left_len == right_len:
            if self.min_heap[0] < num:
                temp = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -temp)
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        else:
            if right_len == 0:
                if num > -self.max_heap[0]:
                    heapq.heappush(self.min_heap, num)
                else:
                    temp = heapq.heappop(self.max_heap)
                    heapq.heappush(self.min_heap, -temp)
                    heapq.heappush(self.max_heap, -num)
            elif num < -self.max_heap[0]:
                temp = heapq.heappop(self.max_heap)
                heapq.heappush(self.max_heap, -num)
                heapq.heappush(self.min_heap, -temp)
            else:
                heapq.heappush(self.min_heap, num)

    def findMedian(self) -> float:

        median, mid = 0, 0
        if not self.max_heap and not self.min_heap:
            return None
        # arr_len = len(self.max_heap) + len(self.min_heap)

        if len(self.max_heap) > len(self.min_heap):
            median = float(-self.max_heap[0])
        else:
            median = (-self.max_heap[0] + self.min_heap[0]) / 2

        # print(median,self.arr, arr_len)
        return median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()