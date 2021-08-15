#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def makeFancyString(self, s: str) -> str:
        a = []
        for c in s:
            if not a:
                a.append(c)
            else:
                if len(a) < 2:
                    a.append(c)
                else:
                    if a[-1] == c and a[-2] == c:
                        continue
                    else:
                        a.append(c)
        return "".join(a)
