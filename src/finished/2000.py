#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        print("word=", word[0:3:-1])
        idx = 0
        try:
            idx = word.index(ch)
        except:
            pass
        return word[0:idx + 1:-1] + word[idx + 1:]
