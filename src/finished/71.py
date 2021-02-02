#  Copyright (c) 2021
#  @Author: xiaoweixiang
from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        先以/为分隔符，分割，然后再入栈
        然后再记录要回归几层
        :param path:
        :return:
        """
        print("path: ", path)
        a = path.split('/')
        print(a)
        stack = deque()
        for s in a:
            stack.append(s)
        ans = ""
        c = 0
        while len(stack) > 0:
            t = stack.pop()
            if t == "": continue
            if t == "..":
                c += 1
            elif t == ".":
                continue
            else:
                if c == 0:
                    ans += "/" + t
                else:
                    c -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    path = "/home//foo/"
    res = solution.simplifyPath(path)
    print(res)
