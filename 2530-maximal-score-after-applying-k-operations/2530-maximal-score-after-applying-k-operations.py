class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans=[]
        for i in nums:
            ans.append(-1*i)
        solution=0
        heapify(ans)
        while k:
            value=-1*heappop(ans)
            solution+=value
            heappush(ans,-1*(math.ceil(value/3)))
            k-=1
            
            
        return solution
            