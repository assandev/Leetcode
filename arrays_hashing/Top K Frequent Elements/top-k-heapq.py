import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for number in nums:
            freq[number] = freq.get(number, 0) + 1
        
        print(freq)
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)
        
        return [num for count, num in heap]