class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_mult = [1 for _ in range(len(nums))]
        right_mult = [1 for _ in range(len(nums))]
        
        left_mult[0]= nums[0]
        
        right_mult[-1] = nums[-1]
        
        ans =[1 for _ in range(len(nums))]
        
        for index in range(1,len(nums)):
            left_mult[index]= left_mult[index-1]*nums[index]
        
        for index in range(len(nums)-2,-1,-1):
            right_mult[index]=right_mult[index+1]*nums[index]
        
        ans[0]=right_mult[1]
        ans[-1]= left_mult[-2]
        
        for i in range(1,len(nums)-1):
            ans[i]=left_mult[i-1]* right_mult[i+1]
        return ans
        