#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(3, len(nums)):
            for j in range(i - 1, 1, -1):
                for k in range(j - 1, 0, -1):
                    for m in range(k - 1, -1, -1):
                        if nums[i] == nums[j] + nums[k] + nums[m]:
                            cnt += 1
        return cnt
