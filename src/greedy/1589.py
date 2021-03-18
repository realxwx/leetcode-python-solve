#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        counts = [0 for _ in range(len(nums))]
        for start, end in requests:
            counts[start] += 1
            if end + 1 < len(nums):
                counts[end + 1] -= 1
        for i in range(1, len(nums)):
            counts[i] += counts[i - 1]
        nums.sort(reverse=True)
        counts.sort(reverse=True)
        j = 0
        ans = 0
        for n in counts:
            ans += n * nums[j]
            j += 1
        return ans % (10 ** 9 + 7)
