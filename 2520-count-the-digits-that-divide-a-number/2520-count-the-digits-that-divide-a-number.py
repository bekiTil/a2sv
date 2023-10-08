class Solution:
    def countDigits(self, num: int) -> int:
        val = str(num)
        count = 0
        for i in val:
            if num%(int(i)) ==0:
                count +=1
        return count