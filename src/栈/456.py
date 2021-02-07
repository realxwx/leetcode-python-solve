#  Copyright (c) 2021
#  @Author: xiaoweixiang
from collections import deque
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        暴利破解
        用栈怎么解决呢，单调栈
        :param nums:
        :return:
        """
        max_value = float('-inf')
        secend_max_value = float('-inf')
        q = deque()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < secend_max_value:
                return True
            while len(q) > 0 and nums[i] > q[-1]:
                secend_max_value = max(secend_max_value, q.pop())
            q.append(nums[i])
        return False


if __name__ == '__main__':
    nums = [3, 1, 4, 2]
    solution = Solution()
    ans = solution.find132pattern(nums)
    print("ans:", ans)
