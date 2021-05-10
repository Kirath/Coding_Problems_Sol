from collections import Counter
import heapq

def reorganizeString(S):
    max_heap = []
    char_count = Counter(S)
    res = ''
    print(char_count)
    heapq.heapify(max_heap)
    for i in char_count:
        heapq.heappush(max_heap, (-char_count[i], i))
    # print(max_heap)
    while len(max_heap) > 1:
        freq1, char1 = heapq.heappop(max_heap)
        freq2, char2 = heapq.heappop(max_heap)
        freq1 += 1
        freq2 += 1
        res += char1 + char2
        if -freq1 > 0:
            heapq.heappush(max_heap, (freq1, char1))
        if -freq2 > 0:
            heapq.heappush(max_heap, (freq2, char2))
        # print(res, max_heap)
    if max_heap:
        freq, last = heapq.heappop(max_heap)
        print(last)
        if -freq > 1:
            return ''
        res += last
    return res



print(reorganizeString('aaab'))