class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missed=0
        for index,value in enumerate(nums):
            missed^=(index+1)
            missed^=value
        return missed
            