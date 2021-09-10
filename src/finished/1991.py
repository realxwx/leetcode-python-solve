#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        for i in range(1, len(nums) - 1):
            if sum(nums[0:i]) == sum(nums[i + 1:]): return i
        if sum(nums[0:-1]) == 0: return len(nums) - 1
        return -1
