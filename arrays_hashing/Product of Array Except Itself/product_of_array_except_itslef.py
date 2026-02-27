from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Prefix | Finding product of left items
        for num in range(1, n):
            output[num] = output[num-1] * nums[num-1]
        
        # Sufix | Finding product of right items
        sufix = 1
        for num in range(n-1, -1, -1):
            output[num] *= sufix 
            sufix *= nums[num]
        
        return output