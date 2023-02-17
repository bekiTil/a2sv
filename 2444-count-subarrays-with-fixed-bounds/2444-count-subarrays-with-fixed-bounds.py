class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        kmin, kmax, start,ans  = 0, 0, -1,0
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                kmin, kmax, start = 0, 0, i
            else:
                if num == minK:
                    kmin = i - start
                if num == maxK:
                    kmax = i - start            
                ans += min(kmin, kmax)
        return ans