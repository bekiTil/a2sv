class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            while b>0:
                temp=a
                a=b
                b=temp%b
            return a
        ans=min(nums)
        ans1=max(nums)
        
        return gcd(ans,ans1)
        