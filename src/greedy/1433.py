#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        """
        排序后比较
        :param s1:
        :param s2:
        :return:
        """
        s1 = sorted(s1)
        s2 = sorted(s2)
        print("s1=", s1)
        print("s2=", s2)
        ans = True
        for i in range(len(s1)):
            if s1[i] < s2[i]:
                ans = False
                break
        ans1 = True
        for i in range(len(s1)):
            if s1[i] > s2[i]:
                ans1 = False
                break
        return ans or ans1


if __name__ == '__main__':
    solution = Solution()
    s1 = "abc"
    s2 = "xya"
    res = solution.checkIfCanBreak(s1, s2)
    print("res=", res)
