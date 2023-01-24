class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr=[0]*len(nums)
        
        for i,j in requests:
            arr[i]+=1
            if j+1<len(nums):
                arr[j+1]-=1
        for i in range(1,len(arr)):
            arr[i]+=arr[i-1]
        arr.sort()
        nums.sort()
        total=0
        mod=10**9 + 7
        print(arr)
        print(nums)
        for i in range(len(nums)):
            total+=(nums[i]*arr[i])
            
           
        return total % mod