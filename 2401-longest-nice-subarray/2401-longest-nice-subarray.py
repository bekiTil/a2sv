class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
       
        left = 0
        number = 0
        maximum = 0
        for right in range(len(nums)):
            
            while number & nums[right]:
                number^= nums[left]
                left+=1
            maximum = max(maximum,right-left+1)
            number|= nums[right]
        return maximum
            
            
                