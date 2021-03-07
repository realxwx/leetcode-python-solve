#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        for i in range(len(word1)):
            if i < len(word2):
                s += word1[i] + word2[i]
            else:
                s += word1[i]
        if len(word2) > len(word1):
            s += word2[len(word1):]
        return s
