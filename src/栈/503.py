#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        a = []
        b = []
        for num in nums[::-1]:
            while len(a) > 0 and num >= a[-1]:
                a.pop()
            if len(a) > 0:
                b.append(a[-1])
            else:
                b.append(-1)
            a.append(num)
        # print("a:",a)
        print("b:", b)
        c = b[::-1]
        for i in range(len(c) - 1, -1, -1):
            if c[i] == -1:
                print("i:", i, ",c[i]:", c[i])
                d = nums[i:] + nums[0:i]
                for j in range(1, len(d)):
                    if d[j] > d[0]:
                        c[i] = d[j]
                        print("c:", c)
                        break
        return c


if __name__ == '__main__':
    nums = [5, 4, 3, 2, 1]
    solution = Solution()
    ans = solution.nextGreaterElements(nums)
    print("ans:", ans)
