#  Copyright (c) 2021
#  @Author: xiaoweixiang

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        """
        假设最长的串是从i到j，那么j+1可以根据j判断
        :param s:
        :return:
        """

        def isNice(ss: str) -> bool:
            for ii in range(len(ss)):
                if ss[ii].islower():
                    c = ss[ii]
                    if c.upper() not in ss:
                        return False
                else:
                    c = ss[ii]
                    if c.lower() not in ss:
                        return False
            return True

        length = len(s)
        dp = [[False for _ in range(length)] for _ in range(length)]
        ans = [0, 0]
        for i in range(length):
            for j in range(i + 1, length):
                if dp[i][j - 1]:
                    s1 = s[i:j]
                    if s[j] in s1:
                        dp[i][j] = True
                        if j - i > ans[1] - ans[0]:
                            ans = [i, j]
                else:
                    s1 = s[i:j + 1]
                    if isNice(s1):
                        dp[i][j] = True
                        if j - i > ans[1] - ans[0]:
                            ans = [i, j]
        return s[ans[0]:ans[1] + 1] if ans[1] != 0 else ""


if __name__ == '__main__':
    solution = Solution()
    s = "YazaAay"
    res = solution.longestNiceSubstring(s)
    print("res=", res)
