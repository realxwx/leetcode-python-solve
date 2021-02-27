#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
        记录个数、字符串、起始位置
        :param source:
        :param target:
        :return:
        """
        dp = [[0, len(source)] for _ in range(len(target))]
        for i in range(len(target)):
            if i == 0:
                idx = source.find(target[i])
                if idx == -1:
                    return -1
                else:
                    dp[0] = [1, idx]
            else:
                idx = source.find(target[i], dp[i - 1][1] + 1)
                if idx == -1:
                    idx = source.find(target[i])
                    if idx == -1:
                        return -1
                    else:
                        dp[i] = [dp[i - 1][0] + 1, idx]
                else:
                    dp[i] = [dp[i - 1][0], idx]
        return dp[len(dp) - 1][0]
