#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        a = text.split("")
        cnt = len(a)
        for s in a:
            for k in s:
                if k in brokenLetters:
                    cnt -= 1
                    break
        return cnt
