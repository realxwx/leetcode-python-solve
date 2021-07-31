#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        m0, m1 = 0, 0
        idx = 0
        ans = []
        while idx < len(s):
            t = s[idx]
            le = 1
            while idx + 1 < len(s) and s[idx + 1] == t:
                le += 1
                idx += 1
            ans.append([le, t])
            idx += 1
        print(ans)
        ans.sort(reverse=True)
        if len(ans) == 1:
            return True if ans[0][1] == "1" else False
        if ans[0][1] == "0":
            return False
        a = ans[0][0]
        b = ans[0][1]
        for k in range(1, len(ans)):
            if ans[k][0] == a and ans[k][1] == "0":
                return False
            if a > ans[k][0]:
                break
        return True
