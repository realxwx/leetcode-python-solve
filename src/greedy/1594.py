#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:

    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        row = len(grid)
        col = len(grid[0])
        # large
        dp0 = [[0 for _ in range(col)] for _ in range(row)]
        # small
        dp1 = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                t = grid[i][j]
                print("i=", i, ",j=", j, ",t=", t)
                if i == 0 and j == 0:
                    if t == 0:
                        dp0[i][j] = 0
                        dp1[i][j] = 0
                    elif t > 0:
                        dp0[i][j] = t
                        dp1[i][j] = t
                    else:
                        dp0[i][j] = t
                        dp1[i][j] = t
                elif i == 0 and j > 0:
                    if t == 0:
                        dp0[i][j] = 0
                        dp1[i][j] = 0
                    elif t > 0:
                        dp0[i][j] = t * dp0[i][j - 1]
                        dp1[i][j] = t * dp1[i][j - 1]
                    else:
                        dp0[i][j] = dp1[i][j - 1] * t
                        dp1[i][j] = t * dp0[i][j - 1]
                elif i > 0 and j == 0:
                    if t == 0:
                        dp0[i][j] = 0
                        dp1[i][j] = 0
                    elif t > 0:
                        dp0[i][j] = t * dp0[i - 1][j]
                        dp1[i][j] = t * dp1[i - 1][j]
                    else:
                        dp0[i][j] = dp1[i - 1][j] * t
                        dp1[i][j] = t * dp0[i - 1][j]
                else:
                    if t == 0:
                        dp0[i][j] = 0
                        dp1[i][j] = 0
                    elif t > 0:
                        dp0[i][j] = t * max(dp0[i - 1][j], dp0[i][j - 1])
                        dp1[i][j] = t * min(dp1[i - 1][j], dp1[i][j - 1])
                    else:
                        dp0[i][j] = t * min(dp1[i - 1][j], dp1[i][j - 1])
                        dp1[i][j] = t * max(dp0[i - 1][j], dp0[i][j - 1])
        print("dp0=", dp0)
        print("dp1=", dp1)
        return dp0[-1][-1] % MOD if dp0[-1][-1] >= 0 else -1


if __name__ == '__main__':
    solution = Solution()
    grid = [[1, 3], [0, -4]]
    ans = solution.maxProductPath(grid)
    print("ans=", ans)
