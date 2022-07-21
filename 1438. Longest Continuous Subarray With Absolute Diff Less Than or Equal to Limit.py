

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mini=deque([])
        maxi=deque([])
        memo=defaultdict(int)
        k=0
        maxs=float("-inf")
        for index,i in enumerate(nums):
            while maxi and maxi[-1]<i:
                maxi.pop()
            while mini and mini[-1]>i:
                mini.pop()
            maxi.append(i)
            mini.append(i)
            memo[i]+=1
            while maxi and memo[maxi[0]]==0:
                maxi.popleft()
            while mini and memo[mini[0]]==0:
                mini.popleft()
            if maxi[0]-mini[0]>limit:
                maxs=max(maxs,index-k)
                memo[nums[k]]-=1
                k+=1
        # print(index)
        # print(k)
        
        maxs=max(maxs,index+1-k)
        return maxs
                
