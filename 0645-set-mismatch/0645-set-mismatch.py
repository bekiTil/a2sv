class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count=defaultdict(int)
        n=len(nums)
        ans=[]
        for i in nums:
            count[i]+=1
            if count[i]>1:
                ans.append(i)
                break
        nums=set(nums)
        for i in range(1,n+1):
            if i not in nums:
                ans.append(i)
                return ans
            