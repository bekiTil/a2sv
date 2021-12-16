def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        new=[]
        rem=0
        start=len(nums)-1
        while len(nums)!=len(new):
            new.append(nums[rem])
            rem+=1
            if start>rem:
                new.append(nums[start])
                start-=1
        return new
