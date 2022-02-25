class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i,j=0,len(nums)-1
        r,l=0,len(nums)-1
        new=-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                new=mid
                j=mid-1
            elif nums[mid] >target:
                j=mid-1
            else:
                i=mid+1
        
        answer=[]
        answer.append(new)
        new=-1
        while r<=l:
            mid=(r+l)//2
            if nums[mid]==target:
                new=mid
                r=mid+1
            elif nums[mid]>target:
                l=mid-1
            else:
                r=mid+1
        answer.append(new)
        return answer
                
