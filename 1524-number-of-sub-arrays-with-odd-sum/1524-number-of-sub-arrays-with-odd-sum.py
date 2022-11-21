class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count=defaultdict(int)
        prefix=[0]
        for i in arr:
            prefix.append(prefix[-1]+i)
        ans=0
        for i in prefix:
            if i%2==0:
                ans+=count[1]
                count[0]+=1
            else:
                ans+=count[0]
                count[1]+=1
        return ans % (10**9 + 7)