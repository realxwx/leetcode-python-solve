#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a = ""
        for d in firstWord:
            print(ord(d))
            a += str(ord(d) - ord('a'))
        b = ""
        for d in secondWord:
            b += str(ord(d) - ord('a'))
        c = ""
        for d in targetWord:
            c += str(ord(d) - ord('a'))
        return int(c) == int(a) + int(b)
