class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        step=0
        i=0
        zero=0
        maximum=float("-inf")
        while i<len(nums):
            if zero==k:
                if nums[i]==1:
                    pass
                else:
                    maximum=max(maximum,i-step)
                    
                    if nums[step]==0:
                        zero-=1
                        step+=1
                        i-=1
                    else:
                        step+=1
                        i-=1
            elif nums[i]==0:
                zero+=1
            
            i+=1
        maximum=max(maximum,i-step)
        return maximum
                
