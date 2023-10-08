class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new=0
        for i in nums:
            new=new^i
       
        return new