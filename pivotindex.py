class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        new=[0]*len(nums)
        past=[0]*len(nums)
        just=list(reversed(nums))
        for i in range(len(nums)-1):
            new[i+1]=nums[i]+new[i]
        
        for i in range(len(nums)-1):
            past[i+1]=just[i]+past[i]
        past.reverse()
       
        for i in range(len(nums)):
            if past[i]==new[i]:
                return i 
        return -1
