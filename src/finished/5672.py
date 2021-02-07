#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        a = nums[:]
        a.sort()
        for i in range(len(nums)):
            b = nums[i:len(nums)] + nums[0:i]
            if a == b:
                return True
        return False
