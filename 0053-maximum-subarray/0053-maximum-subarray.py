class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        mini=0
        
        ans=float('-inf')
        for i in nums:
            ans=max(ans, i-mini)
            mini=min(mini,i)
        return ans
        