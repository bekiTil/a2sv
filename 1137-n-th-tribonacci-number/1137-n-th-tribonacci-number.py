class Solution:
    def tribonacci(self, n: int) -> int:
        a=0
        b=1
        c=1
        if n<=2:
            if n==2:
                return c
            elif n==1:
                return b
            else:
                return a
        else:
            while n>2:
                c,b,a=a+b+c,c,b
                n-=1
        return c 