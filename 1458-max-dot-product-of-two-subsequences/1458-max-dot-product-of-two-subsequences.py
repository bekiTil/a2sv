class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[0 for _ in range(len(nums1)+1)] for _ in range(len(nums2)+1)]
        
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                taken=dp[i][j]+nums1[j]*nums2[i]
                
                dp[i+1][j+1]=max(taken,dp[i][j+1],dp[i+1][j])
       
        if dp[-1][-1]==0:
            return max(max(nums1)*min(nums2),max(nums2)*min(nums1))
     
        return dp[-1][-1]