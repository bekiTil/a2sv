class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(a,b):
            if a<b:
                a,b=b,a
            while b>0:
                rem=a%b
                a=b
                b=rem
            return a
        temp=nums[0]
        for i in nums[1:]:
            temp=gcd(temp,i)
        if temp!=1:
            return False
        return True
            