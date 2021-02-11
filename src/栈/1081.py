#  Copyright (c) 2021
#  @Author: xiaoweixiang
from collections import deque


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        q = deque()
        for i in range(len(s)):
            if s[i] in q:
                continue
            while q and q[-1] > s[i] and s.find(q[-1], i) != -1:
                q.pop()
            q.append(s[i])
        return "".join(q)
