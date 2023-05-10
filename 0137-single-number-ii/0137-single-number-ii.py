class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        value = 0
        for i in range(32):
            count = 0
            for val in nums:
                val = abs(val)
                if val & 2 ** i:
                    count+=1
            reminder = count%3
            if reminder !=0:
                value += 2**i
        
        counts = 0
        for val in nums:
            if val == value :
                counts+=1
        if counts>1 or counts ==0:
            return -1 * value
        return value
            
        
     