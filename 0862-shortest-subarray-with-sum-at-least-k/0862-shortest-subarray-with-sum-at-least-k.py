class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix=[0]

        for i in nums:
            prefix.append(prefix[-1]+i)
        
        queue = deque([])
        queue.append(0)
        ans = float("inf")
        for i in range(len(prefix)):
            
            while queue and prefix[i]-prefix[queue[0]] >= k:
                ans = min (ans, i-queue[0])
                queue.popleft()
            while queue and prefix[i]<prefix[queue[-1]]:
                queue.pop()
            queue.append(i)
        if ans == float('inf'):
            return -1
        return ans