#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        """
        参考官方，看了半天终于明白了
        :param S:
        :param K:
        :return:m,
        """
        size = 0
        length = len(S)
        for i in range(length):
            if S[i].isalpha():
                size += 1
            elif S[i].isdigit():
                size *= int(S[i])
        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c
            if c.isdigit():
                size /= int(c)
            else:
                size -= 1


if __name__ == '__main__':
    solution = Solution()
    S = "vzpp636m8y"
    K = 2920
    res = solution.decodeAtIndex(S, K)
    print("res:", res)
