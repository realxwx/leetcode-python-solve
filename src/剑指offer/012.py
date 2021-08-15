#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        t = 0
        for i in range(len(nums)):
            t += nums[i]
            if t == s // 2:
                return i
        return 0 if s == 0 else -1
