#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        """
        都是套路
        栈+动态规划
        :param S:
        :return:
        """
        from collections import deque
        q = deque()
        for i in range(len(S)):
            if S[i] == '(':
                q.append(S[i])
            else:
                tmp = 0
                while len(q) > 0 and q[-1] != '(':
                    tmp += int(q.pop())
                q.pop()
                if tmp == 0:
                    q.append(1)
                else:
                    q.append(2 * tmp)
        print(q)
        return sum(int(i) for i in q)


if __name__ == '__main__':
    solution = Solution()
    S = "(()(()))"
    res = solution.scoreOfParentheses(S)
    print(res)
