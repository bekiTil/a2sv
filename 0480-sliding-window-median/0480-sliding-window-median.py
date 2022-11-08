class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        value=nums[:k-1]
        ans=[]
        for i in range(k-1,len(nums)):
            if i>k-1:
                value.pop(0)
                
            value.append(nums[i])
            
            temp=sorted(value)
            
            if k%2==0:
                ans.append((temp[k//2]+temp[(k//2)-1])/2)
            else:
                ans.append(float(temp[k//2]))
        return ans