#  Copyright (c) 2021
#  @Author: xiaoweixiang
import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        a = collections.Counter(s)
        print("a=", a, ",type=", type(a))
        b = list(a.values())
        print("b=", b, ",type=", type(b))
        b.sort()
        ans = 0
        while b:
            n = b.pop()
            cnt = 1
            while b and b[-1] == n:
                cnt += 1
                b.pop()
            while cnt > 1:
                ans += 1
                b.append(n - 1)
                cnt -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = "aaabbbcc"
    res = solution.minDeletions(s)
    print("res=", res)
