class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        count = defaultdict(int)
        
        extent = defaultdict(lambda : [-1,-1])
        
        maximum = 0
        
        for index, val in enumerate(nums):
            
            count[val]+=1
            if count[val]==1:
                extent[val][0]=index
            extent[val][1]=index
            maximum = max(maximum, count[val])
        
        ans = len(nums)
        for val in count:
            if count[val] == maximum :
                ans = min ( ans, (extent[val][1]- extent[val][0])+1)
        print(ans)
        return ans
        