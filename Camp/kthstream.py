import heapq as hq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        hq.heapify(self.nums)
        n=len(self.nums)
        while n>self.k:
            hq.heappop(self.nums)
            n-=1
        
    def add(self, val: int) -> int:
        hq.heappush(self.nums,val)
        n=len(self.nums)
        while n>self.k:
            hq.heappop(self.nums)
            n-=1
        return self.nums[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
