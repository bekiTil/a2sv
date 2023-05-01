class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        memo = {}
        
        ans = float("inf")
        temp = 0
        j = 0
        for i in range(len(nums)):
            temp += nums[i]
            while temp >= target:
                ans = min (ans, i-j+1)
                temp -= nums[j]
                j+=1
        if ans == float("inf"):
            return 0
        return ans
            