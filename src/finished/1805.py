#  Copyright (c) 2021
#  @Author: xiaoweixiang
from collections import Counter


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        t = ""
        a = []
        for i in range(len(word)):
            if word[i].isalpha():
                if t: a.append(int(t))
                t = ""
            else:
                t += word[i]
        if t: a.append(int(t))
        print("a=", a)
        d = Counter(a)
        print("d=", d)
        print("d.elements()=", d.keys())
        ans = 0
        for j in d.keys():
            print("j=", j)
            if j:
                ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    word = "a123bc34d8ef34"
    res = solution.numDifferentIntegers(word)
    print("res=", res)
