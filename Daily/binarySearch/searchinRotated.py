#Time Complexity O(log(n))

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def checker(medium,front,target):
            if medium==front:
                return False
            elif nums[medium]>=nums[front]:
                if target<nums[medium]:
                    if target<nums[front]:
                        return False
                    return True
                else:
                    return False
            else:
                if target>nums[medium]:
                    if target<nums[front]:
                        return False
                    else:
                        return True
                else:
                    return True
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return True
            elif checker(mid,i,target):
                j-=1
            else:
                i+=1
        return False
