class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        count={}
        
        for i in nums:
            if sqrt(i) in count:
                count[i]=count[sqrt(i)]+1
            else:
                count[i]=1
        
        maximum=0
        for i in count:
           
            maximum=max(maximum,count[i])
        if maximum==1:
            return -1
        return maximum