class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def gcd(a,b):
            if a<b:
                a,b=b,a
            while b>0:
                temp=a
                a=b
                b=temp%b
            return a
        return n*2//(gcd(n,2))