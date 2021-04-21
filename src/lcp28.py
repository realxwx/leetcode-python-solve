#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()
        k = 0
        length = len(nums)
        last = length - 1
        for i in range(length):
            t = target - nums[i]
            if i >= last or t <= 0: break
            for j in range(last, i, -1):
                if nums[j] <= t:
                    last = j
                    k += j - i
                    break

        return k % (10 ** 9 + 7)
