#  Copyright (c) 2021
#  @Author: xiaoweixiang
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        """
        分两步，  第一步把*和/处理掉
                第二步，把+和-处理掉
        :param s:
        :return:
        """
        stack = deque()
        stack1 = deque()
        a = ""
        for i in range(len(s)):
            if s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
                stack.append(a)
                a = ""
                stack.append(s[i])
            elif s[i] == ' ':
                continue
            else:
                a += s[i]
        stack.append(int(a))
        print("stack:", stack)
        while len(stack) > 0:
            t = stack.popleft()
            if t == '*' or t == '/':
                m1 = stack1.pop()
                m2 = stack.popleft()
                print(type(m1))
                print(type(m2))
                print("m1:", m1)
                print("m2:", m2)
                if t == '*':
                    m3 = int(m1) * int(m2)
                else:
                    m3 = int(m1) // int(m2)
                stack.appendleft(m3)
            else:
                stack1.append(t)
        ans = 0
        tmp = 0
        while len(stack1) > 0:
            t1 = stack1.popleft()
            if t1 == '+' or t1 == '-':
                m1 = stack1.popleft()
                if t1 == '+':
                    m3 = int(m1) + int(tmp)
                else:
                    m3 = int(tmp) - int(m1)
                stack1.appendleft(m3)
            else:
                tmp = t1
        return tmp


if __name__ == '__main__':
    solution = Solution()
    s = "1+1+1"
    res = solution.calculate(s)
    print(res)
