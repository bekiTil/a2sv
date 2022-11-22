class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(n)
        dp=[[1,1] for _ in range(len(nums))]
        longest=1
        for i,num in enumerate(nums):
            for j in range(i):
                if nums[j]<num:
                    dp[i][0]=max(dp[i][0],dp[j][0]+1)
            count=0
            for j in range(i):
                if dp[j][0]==dp[i][0]-1 and nums[j]<num:
                    count+=dp[j][1]
            dp[i][1]=max(dp[i][1],count)
            longest=max(longest,dp[i][0])
        ans=0
        for value in dp:
            if value[0]==longest:
                ans+=value[1]
        print(ans)
        return ans