#  Copyright (c) 2021
#  @Author: xiaoweixiang
from collections import deque
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        栈和动态规划的结合体
        :param n:
        :param logs:
        :return:
        """
        q = deque()
        ans = [0 for _ in range(n)]
        for s in logs:
            s_array = s.split(":")
            if s_array[1] == "start":
                q.append(s_array)
            else:
                tmp = q.pop()
                k = int(s_array[2]) - int(tmp[2]) + 1
                ans[int(s_array[0])] += k
                if len(q) > 0:
                    ans[int(q[-1][0])] -= k
        return ans


if __name__ == '__main__':
    n = 2
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    solution = Solution()
    res = solution.exclusiveTime(n, logs)
    print(res)
