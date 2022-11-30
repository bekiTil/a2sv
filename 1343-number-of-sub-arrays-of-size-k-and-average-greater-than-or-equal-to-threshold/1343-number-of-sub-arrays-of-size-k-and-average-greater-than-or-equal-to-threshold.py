class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefix=[0]
        for i in range(len(arr)):
            prefix.append(prefix[-1]+arr[i])
        ans=0
        for i in range(k,len(prefix)):
            if ((prefix[i]-prefix[i-k])/k)>=threshold:
                ans+=1
        return ans