class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sums(arr,num):
            new=0
            for i in arr:
                new+=math.ceil(i/num)
               
            return new
        i=1
        j=max(nums)
        val=1
        while i<=j:
         
            mid=(i+j)//2
            k=sums(nums,mid)
            print(k)
            if k<=threshold:
                val=mid
                j=mid-1
            else:
                i=mid+1
        return val
    
