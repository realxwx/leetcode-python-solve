#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(" ")
        ans = [' ' for _ in range(len(arr))]
        for s in arr:
            for i in range(len(s)):
                if s[i].isdigit():
                    a = s[:i]
                    b = int(s[i:])
                    print("a=", a)
                    print("b=", b)
                    ans[b - 1] = a
        return " ".join(ans)
