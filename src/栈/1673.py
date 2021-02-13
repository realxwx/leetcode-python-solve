#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
            while ans and ans[-1] > nums[i] and n - i > k - len(ans):
                ans.pop()
            if len(ans) < k:
                ans.append(nums[i])
        return ans


if __name__ == '__main__':
    nums = [2, 4, 3, 3, 5, 4, 9, 6]
    k = 4
    solution = Solution()
    res = solution.mostCompetitive(nums, k)
    print("res=", res)
