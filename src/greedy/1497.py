#  Copyright (c) 2021
#  @Author: xiaoweixiang
import collections
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        """
        python 和 Java 在取余上的计算方式不同
        :param arr:
        :param k:
        :return:
        """
        m = collections.defaultdict(int)
        for a in arr:
            b = a % k
            # if a < 0: b = k - b
            m[b] += 1
        for i in range(1, k // 2 + 1):
            if m[i] != m[k - i]: return False
        return m[0] % 2 == 0


if __name__ == '__main__':
    solution = Solution()
    arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
    k = 5
    res = solution.canArrange(arr, k)
    print("res=", res)
