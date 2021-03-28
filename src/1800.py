#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        t, ans = nums[0], 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                t += nums[i]
            else:
                ans = max(ans, t)
                t = nums[i]
        return max(t, ans)
