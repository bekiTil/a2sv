class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        memo={}
        prefix=[0]
        for i in nums:
            prefix.append(prefix[-1]+i)
        for index,i in enumerate(prefix):
            if i%k in memo:
                if index-memo[i%k]>=2:
                    return True
            else:
                memo[i%k]=index
        return False