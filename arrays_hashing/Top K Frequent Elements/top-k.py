from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for number in nums:
            freq[number] = freq.get(number, 0) + 1
        
        sorted_freq = [num for num, _ in sorted(freq.items(), key=lambda p: p[1], reverse=True)[:k]]
        
        return sorted_freq