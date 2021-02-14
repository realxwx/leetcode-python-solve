#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def minOperations(self, s: str) -> int:
        """
        只需要确定第一个字符是0还是1就好了
        :param s:
        :return:
        """
        if not s: return 0
        a = s[0]
        if a == "1":
            count1 = 0
            count2 = 0
            for i in range(1, len(s)):
                if i % 2 == 0:
                    if s[i] != "1":
                        count1 += 1
                else:
                    if s[i] != "0":
                        count1 += 1
            count2 += 1
            for i in range(1, len(s)):
                if i % 2 == 0:
                    if s[i] != "0":
                        count2 += 1
                else:
                    if s[i] != "1":
                        count2 += 1
            return min(count1, count2)
        else:
            count1 = 0
            count2 = 0
            for i in range(1, len(s)):
                if i % 2 == 0:
                    if s[i] != "0":
                        count2 += 1
                else:
                    if s[i] != "1":
                        count2 += 1
            count1 += 1
            for i in range(1, len(s)):
                if i % 2 == 0:
                    if s[i] != "1":
                        count1 += 1
                else:
                    if s[i] != "0":
                        count1 += 1
            return min(count1, count2)
