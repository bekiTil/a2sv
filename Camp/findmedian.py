import heapq as hq
class MedianFinder:

    def __init__(self):
        self.maxheap=[]
        self.minheap=[]

    def addNum(self, num: int) -> None:
        if len(self.maxheap)==0:
            hq.heappush(self.maxheap,-1*num)
        elif num>-1*self.maxheap[0] and len(self.maxheap)>len(self.minheap):
            hq.heappush(self.minheap,num)
        elif num<=-1*self.maxheap[0] and len(self.maxheap)>len(self.minheap):
            hq.heappush(self.minheap,-1*hq.heappop(self.maxheap))
            hq.heappush(self.maxheap,-1*num)
        elif num>self.minheap[0]:
            hq.heappush(self.maxheap,-1*hq.heappop(self.minheap))
            hq.heappush(self.minheap,num)
        else:
            hq.heappush(self.maxheap,-1*num)
                        

    def findMedian(self) -> float:
        if len(self.minheap)==len(self.maxheap):
                        return (-1 * self.maxheap[0]+self.minheap[0])/2
        else:
                        return float(-1* self.maxheap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
