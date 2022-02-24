import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq.heapify(nums)
        print(nums)
        while len(nums)>k:
            hq.heappop(nums)  
        return nums[0]
