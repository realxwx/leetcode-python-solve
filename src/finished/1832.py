#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set()
        for i in sentence:
            s.add(i)
        return len(s) == 26
