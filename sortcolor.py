class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new=[0]*3
        for i in nums:
            new[i]+=1
        j=0
        for i in range(len(new)):
            
            while new[i]>0:
                nums[j]=i
                new[i]-=1
                j+=1
    
        
            
        
            
            
