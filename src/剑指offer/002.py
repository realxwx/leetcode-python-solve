#  Copyright (c) 2021 
#  @Author: xiaoweixiang
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aa = int(a, 2)
        bb = int(b, 2)
        cc = aa + bb
        return bin(cc).replace("0b", "")
