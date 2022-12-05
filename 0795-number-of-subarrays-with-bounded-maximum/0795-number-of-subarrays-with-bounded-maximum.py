class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        maximum=deque([])
        minimum=deque([])
        l=0
        m=0
        ans=0
        temp=0
        for r in range(len(nums)):
            while maximum and nums[maximum[-1]]<=nums[r]:
                maximum.pop()
            maximum.append(r)
            while maximum[0]<l:
                maximum.popleft()
            while l<=r and nums[maximum[0]]>right:
                l=maximum[0]+1
                maximum.popleft()
            ans+=(r-l)+1
            
            while minimum and nums[minimum[-1]]<=nums[r]:
                minimum.pop()
            minimum.append(r)
            while minimum[0]<m:
                minimum.popleft()
            while m<=r and nums[minimum[0]]>left-1:
                m=minimum[0]+1
                minimum.popleft()
            temp+=(r-m)+1
        
        print(ans)
        print(temp)
        return ans - temp
            