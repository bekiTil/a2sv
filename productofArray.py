class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        suffix=1
        p=[]
        s=[]
        n=[]
        nu=list(reversed(nums))
        for i in range(len(nums)):
            if i==0:
                p.append(prefix)
            else:
                prefix*=nums[i-1]
                p.append(prefix)
        
        for i in range(len(nums)):
            if i==0:
                s.append(suffix)
            else:
                suffix*=nu[i-1]
                s.append(suffix)
        s.reverse()
        for i in range(len(nums)):
            n.append(s[i]*p[i])
        return n
        
        
