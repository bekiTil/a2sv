class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new=nums1+nums2
        new.sort()
        print(new)
        if len(new)%2==0:
            return (new[len(new)//2]+new[(len(new)-1)//2])/2
        else:
            return (new[len(new)//2] + new[len(new)//2])/2
        
        