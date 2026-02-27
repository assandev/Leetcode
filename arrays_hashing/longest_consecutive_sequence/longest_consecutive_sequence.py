from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0

        for num in nums:
            if (num - 1) not in num_set:
                # Start of a sequence
                length = 1
                next_number = num + 1

                while next_number in num_set:
                    length += 1
                    next_number += 1
                
                best = max(best, length)
        
        return best

