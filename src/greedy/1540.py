#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t): return False
        """
        easy，算每个字符需要几步，然后判断
        :param s:
        :param t:
        :param k:
        :return:
        """
        arr = []
        count = [0] * 26
        for i in range(len(s)):
            b = ord(s[i])
            c = ord(t[i])
            if b <= c:
                count[c - b] += 1
            else:
                count[26 + c - b] += 1
        for i, _ in enumerate(count[1:], 1):
            m = i + 26 * (count[i] - 1)
            if m > k:
                return False
        return True


if __name__ == '__main__':
    s = "iqssxdlb"
    t = "dyuqrwyr"
    k = 40
    solution = Solution()
    res = solution.canConvertString(s, t, k)
    print("res=", res)
