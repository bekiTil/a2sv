class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        exist = {}
        
        for index, num in enumerate(nums):
            if target-num in exist:
                return [exist[target-num],index]
            exist[num]= index