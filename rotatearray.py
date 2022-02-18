class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums)<=k:
            k=k%len(nums)
        if len(nums)==1:
            return nums
        i=1
        nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]
        
   
