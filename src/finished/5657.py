#  Copyright (c) 2021
#  @Author: xiaoweixiang
from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        for k, v in c.items():
            if v == 1:
                res += k
        return res
