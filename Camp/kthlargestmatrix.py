import heapq as hq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        new=[]
        for i in matrix:
            new.extend(i)
      
        hq.heapify(new)
        n=1
        while n<k:
            hq.heappop(new)
            n+=1
        
        return hq.heappop(new)
