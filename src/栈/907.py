#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        没有一点头绪呢
        跟栈有啥关系呢
        动态规划啊
        看了官方解题：动态规划+技巧
        :param arr:
        :return:
        """
        m = 10 ** 9 + 7
        q = []
        length = len(arr)
        ans = c = 0
        for n in arr:
            count = 1
            while q and n < q[-1][0]:
                tmp = q.pop()
                c -= tmp[0] * tmp[1]
                count += tmp[1]
            q.append([n, count])
            c += n * count
            ans += c
        return ans % m


if __name__ == '__main__':
    solution = Solution()
    arr = [3, 1, 2, 4]
    res = solution.sumSubarrayMins(arr)
    print("res:", res)
