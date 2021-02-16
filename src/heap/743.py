#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        难点在于有没有环
        没思路啊，拓扑排序？

        :param times:
        :param n:
        :param k:
        :return:
        """
        from collections import deque
        q = deque()
        ans = 0
        remain = []
        q.append(k)
        remain.append(k)
        while q:
            length = len(q)
            size = len(remain)
            for _ in range(length):
                t = q.popleft()
                for a, b, c in times:
                    if a == t:
                        if b not in remain:
                            remain.append(b)
                            q.append(b)
                            ans += c
            size1 = len(remain)
            if size1 == size:
                break
        return ans if n == len(remain) else -1


if __name__ == '__main__':
    solution = Solution()
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    res = solution.networkDelayTime(times, n, k)
    print("res=", res)
