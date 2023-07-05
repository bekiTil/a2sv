class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        length  = len(nums)
        
        arr =[0 for _ in range(31)]
        
        for num in nums:
            for i in range(31):
                if 2 ** i & num:
                    arr[i]+=1
        count = 0
        
        for i in range(len(arr)):
            count += (arr[i] * (length-arr[i]))
        return count
        