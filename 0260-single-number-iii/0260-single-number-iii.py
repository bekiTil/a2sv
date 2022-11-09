class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        total=0
        for i in nums:
            total^=i
        
        rightbit= (total & total-1)^total
        
        temp=0
        for i in nums:
            if rightbit & i:
                temp^=i
        ans=[]
        ans.append(temp)
        ans.append(temp^total)
        return ans