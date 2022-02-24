import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nw=[]
        for i in stones:
            hq.heappush(nw,-1*i)
       
        while len(nw)>1:
            n=-1*hq.heappop(nw)
            k=-1*hq.heappop(nw)
            if n>=k:
                new=n-k
            else:
                new=k-n
            if new!=0:
                hq.heappush(nw,-1*new)
        if len(nw)==0:
            return 0
        else:
            if nw[0]<0:
                return -1*nw[0]
            return nw[0]
                
        
