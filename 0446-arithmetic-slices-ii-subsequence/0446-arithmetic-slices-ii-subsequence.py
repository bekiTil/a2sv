class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp=[defaultdict(int) for _ in range(len(nums))]
        
        ans=0
        for i in range(len(nums)):
            for j in range(i):
                difference=nums[i]-nums[j]
                total=0
                if dp[j][difference]!=0:
                    total+=dp[j][difference]
                dp[i][difference]+=(total+1)
                ans+=(total)
        #         print(dp[i],i,(ans,total))
        # print(ans)
        # print(dp)
        return ans