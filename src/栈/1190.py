#  Copyright (c) 2021
#  @Author: xiaoweixiang
from collections import deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        栈，两个栈
        :param s:
        :return:
        """
        a = deque()
        b = deque()
        for i in range(len(s)):
            if s[i] == ")":
                while a[-1] != "(":
                    b.append(a.pop())
                a.pop()
                print("b=", b)
                print("a=", a)
                a.extend(b)
                print("a=", a)
                b = deque()
            else:
                a.append(s[i])
        return "".join(a)


if __name__ == '__main__':
    solution = Solution()
    s = "(u(love)i)"
    ans = solution.reverseParentheses(s)
    print("ans=", ans)
