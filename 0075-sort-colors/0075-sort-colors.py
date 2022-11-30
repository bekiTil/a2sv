class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=defaultdict(int)
        for i in nums:
            count[i]+=1
        value=0
        for i in range(len(nums)):
            while count[value]==0:
                value+=1
            
            nums[i]=value
            count[value]-=1