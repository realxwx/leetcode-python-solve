#  Copyright (c) 2021
#  @Author: xiaoweixiang
import collections


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """
        2021年03月06日14:14:41
        排列组合题，不像是贪心啊
        第一步：先把奇數個的處理了
        第二步：把偶数个的处理了
        :param s:
        :param k:
        :return:
        """
        if len(s) < k: return False
        a = collections.Counter(s)
        print("len s=", len(s))
        print("a=", a)
        print("type(a)=", type(dict(a)))
        b = dict(a)
        odd = 0
        even = 0
        for i, j in b.items():
            if j % 2 == 1:
                odd += 1
                b[i] -= 1
                if b[i] > 0:
                    even += b[i]
            else:
                even += j
        print("even=", even)
        k1 = k - odd
        print("k1=", k1)
        if k1 < 0: return False
        return k1 <= even


if __name__ == '__main__':
    solution = Solution()
    s = "ibzkwaxxaggkiwjbeysz"
    k = 15
    ans = solution.canConstruct(s, k)
    print("ans=", ans)
