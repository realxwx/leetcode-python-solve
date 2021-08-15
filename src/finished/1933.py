#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def isDecomposable(self, s: str) -> bool:
        arr = []
        t = ""
        t += s[0]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                t += s[i]
            if s[i] != s[i - 1]:
                arr.append(t)
                t = s[i]
        arr.append(t)
        cnt = 0
        for k in arr:
            if len(k) == 1:
                return False
            if len(k) == 2:
                cnt += 1
                if cnt > 1:
                    return False
            if len(k) >= 3:
                if len(k) % 3 == 0:
                    pass
                if len(k) % 3 == 1:
                    return False
                if len(k) % 3 == 2:
                    cnt += 1
                    if cnt > 1:
                        return False
        return cnt == 1
