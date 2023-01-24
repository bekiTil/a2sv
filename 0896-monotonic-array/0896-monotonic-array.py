class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        temp=sorted(nums)
        if temp==nums:
            return True
        temp.reverse()
        if temp==nums:
            return True
        return False