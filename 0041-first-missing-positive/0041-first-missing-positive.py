class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        exist=defaultdict(int)
        for i in nums:
            exist[i]+=1
        for i in range(1,max(nums)+2):
            if exist[i]==0:
                return i
        return 1
        
        