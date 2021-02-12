#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        a = A
        from collections import deque
        q = deque()
        for i in range(len(a)):
            if not q or a[q[-1]] > a[i]:
                q.append(i)
        ans = 0
        for i in range(len(a) - 1, -1, -1):
            while q and i < q[-1]:
                q.pop()
            while q and a[q[-1]] <= a[i]:
                t = q.pop()
                ans = max(ans, i - t)
        return ans
