class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked= set()
        value = []
        
        for i,j in enumerate(nums):
            heappush(value,(j,i))
        ans = 0
        while value:
            val,index = heappop(value)
            if index not in marked:
                ans+= val
                marked.add(index)
                marked.add(index-1)
                marked.add(index+1)
        return ans
            