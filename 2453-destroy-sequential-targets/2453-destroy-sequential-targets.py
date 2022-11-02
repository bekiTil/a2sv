class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort()
        arr=[]
        value=defaultdict(int)
        for i in nums:
            value[i%space]+=1
        maximum=0
        temp=-1
        for i in value:
            if value[i]>maximum:
                maximum=value[i]
                temp=i
        for i in nums:
            if temp==i%space:
                return i
            