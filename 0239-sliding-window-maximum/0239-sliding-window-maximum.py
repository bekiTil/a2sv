class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i=0
        j=0
        value=deque([])
        ans=[]
        
        while j<len(nums):
            while value and nums[value[-1]]<nums[j]:
                value.pop()
            value.append(j)
            if j-i+1==k:
                while value[0]<i:
                    value.popleft()
                ans.append(nums[value[0]])
                i+=1
            j+=1
            
        return ans
        