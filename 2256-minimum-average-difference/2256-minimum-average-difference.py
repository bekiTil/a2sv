class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        n=len(nums)
        minimum=float('inf')
        index=0
        for i in range(len(nums)):
            av1=nums[i]//(i+1)
            if n==(i+1):
                av2=0
            else:
                av2=(nums[-1]-nums[i])//(n-(i+1))
            # print(av1,av2)
            if minimum>abs(av1-av2):
                index=i
                minimum=abs(av1-av2)
        return index