#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        先处理大的数，然后观察是否最大和第二大之间是否可以是倍数关系
        :param nums:
        :return:
        """
        cnt = 0
        while True:
            maxn = 0
            for i, num in enumerate(nums):

                if num % 2 == 1:
                    cnt += 1
                    nums[i] -= 1
                    maxn = max(maxn, nums[i])
                else:
                    maxn = max(maxn, nums[i])
            print("nums=", nums)
            print("maxn=", maxn)
            if maxn > 0:
                cnt += 1
                for i, _ in enumerate(nums):
                    nums[i] //= 2
            else:
                break
        return cnt


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 5]
    ans = solution.minOperations(nums)
    print("ans=", ans)
