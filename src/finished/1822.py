#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for i in nums:
            if i > 0:
                res *= 1
            elif i < 0:
                res *= -1
            else:
                return 0
        return res
