#  Copyright (c) 2021
#  @Author: xiaoweixiang
from collections import deque


class Solution:
    def minInsertions(self, s: str) -> int:
        q = deque()
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                q.append(s[i])
            else:
                if q and q[-1] == ")":
                    q.pop()
                    if q and q[-1] == "(":
                        q.pop()
                        continue
                    else:
                        count += 1
                else:
                    q.append(s[i])
        print("q=", q)
        print("count=", count)
        while q:
            t = q.pop()
            if t == "(":
                count += 2
            elif t == ")":
                if q and q[-1] == "(":
                    count += 1
                    q.pop()
                else:
                    count += 2
        return count


if __name__ == '__main__':
    s = "(()))(()))()())))"
    solution = Solution()
    ans = solution.minInsertions(s)
    print(ans)
