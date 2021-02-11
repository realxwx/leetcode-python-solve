#  Copyright (c) 2021
#  @Author: xiaoweixiang
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        """
        反向思维，s能否变成""
        :param s:
        :return:
        """
        q = deque()
        for i in range(len(s)):
            if s[i] != 'c':
                q.append(s[i])
            else:
                if len(q) >= 2 and q[-1] == 'b' and q[-2] == 'a':
                    q.pop()
                    q.pop()
                else:
                    return False
        return len(q) == 0
