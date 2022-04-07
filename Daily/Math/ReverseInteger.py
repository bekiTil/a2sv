class Solution:
    def reverse(self, x: int):
        new=len(str(x))
        ans=0
        negative=False
        if x<0:
            x=-1*x
            new-=1
            negative=True
        while new>0:
            reminder=x%10
            ans+=(reminder*(10 **(new-1)))
            x=x//10
            new-=1
        if negative:
            ans=-1*ans
        if ans>((2**31) -1):
            return 0
        elif ans<((-1*2**31)):
            return 0
        return ans
