#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            t = nums[i - 1] - nums[i] + 1
            if t >= 1:
                k += t
                nums[i] += t
        return k
