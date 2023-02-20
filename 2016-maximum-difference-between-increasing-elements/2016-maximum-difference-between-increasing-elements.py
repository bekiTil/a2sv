class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maximum = -1
        
        mini=nums[0]
        
        for i in range(1,len(nums)):
            maximum = max(nums[i]-mini,maximum)
            
            mini = min( mini, nums[i])
        if maximum ==0:
            maximum-=1
        return maximum