#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        套路
        栈+动态规划
        :param asteroids:
        :return:
        """
        from collections import deque
        q = deque()
        ans = []
        for n in asteroids:
            if n < 0:
                if len(q) == 0:
                    q.append(n)
                else:
                    while len(q) > 0:
                        t = q.pop()
                        if t < 0:
                            q.append(t)
                            q.append(n)
                            break
                        else:
                            if t + n > 0:
                                q.append(t)
                                break
                            elif t + n == 0:
                                break
                            elif t + n < 0:
                                if len(q) == 0:
                                    q.append(n)
                                    break
            else:
                q.append(n)
        ans.extend(q)
        return ans


if __name__ == '__main__':
    asteroids = [5, 10, -5]
    solution = Solution()
    res = solution.asteroidCollision(asteroids)
    print(res)
