class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def duplictionChecker(arr,num):
            count=0
            for i in arr:
                if i<=num:
                    count+=1
            
            return (count>num)
        i=1
        j=len(nums)-1
       
        while i<=j:
            mid=(i+j)//2
            if duplictionChecker(nums,mid):
                print(mid)
                new=mid
                j=mid-1
            else:
                i=mid+1
        return new
