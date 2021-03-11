#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        mi = [0 for _ in range(n)]
        ma = [0 for _ in range(n)]
        if nums[0] > 0:
            ma[0] = 1
        elif nums[0] < 0:
            mi[0] = 1
        for i in range(1, n):
            if nums[i] > 0:
                ma[i] = ma[i - 1] + 1
                if mi[i - 1] > 0:
                    mi[i] = mi[i - 1] + 1
            elif nums[i] < 0:
                mi[i] = ma[i - 1] + 1
                if mi[i - 1] > 0:
                    ma[i] = mi[i - 1] + 1
                else:
                    ma[i] = 0

            else:
                mi[i] = 0
                ma[i] = 0
        print("mi=", mi)
        print("ma=", ma)
        return max(ma)


if __name__ == '__main__':
    nums = [1, -2, -3, 4]
    solution = Solution()
    ans = solution.getMaxLen(nums)
    print("ans=", ans)
