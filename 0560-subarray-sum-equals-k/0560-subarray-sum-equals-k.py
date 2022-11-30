class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        count[0]+=1
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        ans=0
        for i in range(len(nums)):
            ans+=count[nums[i]-k]
            count[nums[i]]+=1
        return ans