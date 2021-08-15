#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        total = sum(nums)
        if total % 2 == 1: return False
        t = 0
        for i in nums:
            t += i
            if t == total // 2:
                return True
        return False
