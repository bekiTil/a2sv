class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=defaultdict(int)
        
        for i in nums:
            count[i]+=1
        
        temp=0
        for i in count:
            if i > 0:
                temp+=1
        return temp
                