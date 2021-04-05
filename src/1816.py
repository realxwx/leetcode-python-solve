#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        cnt = 0
        for i in range(len(s)):
            if s[i] == " ":
                cnt += 1
                if cnt == k:
                    return s[:i]
        return s
