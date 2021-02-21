#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        """
        定义方程式，然后求解
        :param s:
        :return:
        """
        ans, start, end = [i + 1 for i in range(len(s) + 1)], 0, 0
        for i in range(len(s)):
            print("ans=", ans)
            if s[i] == "I":
                print("s=", s, ",start=", start, ",end=", end, "i =", i)
                ans = ans[0:start] + ans[start:end + 1][::-1] + ans[end + 1:]
                end += 1
                start = end
            else:
                end += 1
        return ans[0:start] + ans[start:end + 1][::-1] + ans[end + 1:]


if __name__ == '__main__':
    s = "DDIIDI"
    solution = Solution()
    res = solution.findPermutation(s)
    print("res=", res)
