class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        val=list(set(nums))
        val.sort()
        if len(val)-3<0:
            return val[-1]
        else:
            return val[len(val)-3]
        