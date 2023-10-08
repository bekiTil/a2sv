class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        j=n
        while i<=j:
            mid=(i+j)//2
            if n==(mid*(mid+1))//2:
                return mid
            elif n>(mid*(mid+1))//2:
                i=mid+1
            else:
                j=mid-1
        if  n<(mid*(mid+1))//2:
            return mid-1
        else:
            return mid
        return mid