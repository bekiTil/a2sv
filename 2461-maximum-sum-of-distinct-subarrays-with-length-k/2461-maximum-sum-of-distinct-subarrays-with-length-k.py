class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix=[0]
        for i in nums:
            prefix.append(prefix[-1]+i)
        maxi=0
        prefix=prefix[1:]
        visited=set()
        memo=defaultdict(int)
        
        for i in range(k):
            visited.add(nums[i])
            memo[nums[i]]+=1
        
        if len(visited)==k:
            maxi=max(maxi,prefix[k-1])
        

        for i in range(k,len(nums)):
            
            memo[nums[i-k]]-=1
            
            if memo[nums[i-k]]==0:
                visited.remove(nums[i-k])
            
            memo[nums[i]]+=1
            visited.add(nums[i])
            
            if len(visited)==k:
                maxi=max(maxi,prefix[i]-prefix[i-k])
        return maxi