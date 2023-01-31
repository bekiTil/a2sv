class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        temp = []
        size = 0
        for x in nums:
            ans=-1
            i=0
            j=len(temp)-1
            while i<=j:
                mid=(i+j)//2
                if temp[mid]>=x:
                    ans=mid
                    j=mid-1
                else:
                    i=mid+1
            if ans!=-1:
                temp[ans]=x
            else:
                temp.append(x)
        return len(temp)>=len(nums)-1