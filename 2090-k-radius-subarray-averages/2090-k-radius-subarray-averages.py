class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix=[0]
        for i in range(len(nums)):
            prefix.append(prefix[-1]+nums[i])
        
        
        ans=[]
        for i in range(1,len(prefix)):
            if i-k-1<0 or i+k>=len(prefix):
                ans.append(-1)
            else:
                ans.append((prefix[i+k]-prefix[i-k-1])//(2*k+1))
        return ans