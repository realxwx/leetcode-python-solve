#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        cnt = 0
        j = -1
        if len(nums) <= 2: return True
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                cnt += 1
                j = i - 1
                break
        if cnt == 0: return True
        arr = nums[:j] + nums[j + 1:]
        arr1 = nums[:j + 1] + nums[j + 2:]
        aa = True
        aa1 = True
        for k in range(1, len(arr)):
            if arr[k] <= arr[k - 1]:
                aa = False
                break
        for k in range(1, len(arr1)):
            if arr1[k] <= arr1[k - 1]:
                aa1 = False
                break
        return aa or aa1
