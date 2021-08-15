#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for c in s:
            if c.isalnum():
                t += c
        t = t.lower()
        return t == t[::-1]
