class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        mini=[]
        for i in nums:
            if mini:
                if mini[-1]>i:
                    mini.append(i)
                else:
                    mini.append(mini[-1])
            else:
                mini.append(i)
        
        maximum=0    
        for i in range(len(nums)):
            left=0
            right=i-1
            temp=i
            while left<=right:
                mid=(left+right)//2
                if mini[mid]<=nums[i]:
                    temp=mid
                    right=mid-1
                else:
                    left=mid+1
            maximum=max(maximum,i-temp)
        return maximum
        
                    
                    
                