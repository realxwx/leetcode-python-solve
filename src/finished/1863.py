#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        arr = []
        ans = 0
        for n in nums:
            ans += n
            tmp = []
            for i in arr:
                tmp.append(i)
                b = i ^ n
                tmp.append(b)
                ans += b
        return ans
