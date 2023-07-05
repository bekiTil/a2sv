class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count =0    
        for i in range(31):
            if 2 ** i & x != 2 ** i & y:
                count+=1
        return count
            