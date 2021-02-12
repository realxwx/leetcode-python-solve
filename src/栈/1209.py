#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        from collections import deque
        q = deque()
        for i in range(len(s)):
            if not q or q[-1][0] != s[i]:
                q.append([s[i], 1])
            elif q[-1][0] == s[i]:
                if q[-1][1] < k - 1:
                    t = q.pop()
                    q.append([s[i], t[1] + 1])
                else:
                    q.pop()
        ans = ""
        for i, j in q:
            ans += i * j
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = "deeedbbcccbdaa"
    k = 3
    ans = solution.removeDuplicates(s, k)
    print("ans=", ans)
