#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def maxA(self, N: int) -> int:
        """
        2021-02-23 21:32:36
        一点思路也没有。。。。。。
        悲剧
        2021-02-27 11:54:31
        参考了其他人的思路
        :param N:
        :return:
        """
        dp = [0 for _ in range(N + 1)]
        for i in range(1, N + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i - 2, -1, -1):
                dp[i] = max(dp[i], dp[j] * (i - j - 2 + 1))
        return dp[N]
