class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        total =0
        
        column=len(nums[0])
        while column>0:
            value= []
            for i in nums:
                
                i.sort()
                val=i[len(i)-1]
                i[len(i)-1]=0
                heappush(value,-1*val)
                
            total+=(-1*heappop(value))
            column-=1
        
        return total
            