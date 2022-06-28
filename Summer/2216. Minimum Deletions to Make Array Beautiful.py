class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ans=0
        i=0
        j=1
        
        if j==len(nums):
            ans+=1
            return ans
        while j<len(nums):
            if nums[i]==nums[j]:
                ans+=1
                j+=1
            else:
                i=j+1
                j+=2
        if (len(nums)-ans)%2!=0:
            ans+=1
        return ans
