class Solution:
    def addBinary(self, a: str, b: str) -> str:
        one=int(a, 2) 
        two=int(b,2)
        total=bin(one+two)
        return total[2:]