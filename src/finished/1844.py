#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            if s[i].isdigit():
                ans += chr(ord(s[i - 1]) + int(s[i]))
            else:
                ans += s[i]
        return ans
