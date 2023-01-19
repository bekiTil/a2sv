class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix=[0]
        memo=defaultdict(int)
        for i in nums:
            prefix.append(prefix[-1]+i)
        ans=0
        for i in prefix:
            ans+=memo[i%k]
            memo[i%k]+=1
        return ans
        