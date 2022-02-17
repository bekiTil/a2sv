class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        new=set()
        nums.sort()
        j=0
        increment=0
        for i in nums:
            if i in new:
                g=(j-i)+1
                new.add(i+g)
                j=i+g
                increment+=g
            else:
                new.add(i)
                j=i
        
        return increment
        
