class Solution:
    def fib(self, n: int) -> int:
        one=0
        two=1
        if n==0:
            return 0
        elif n==1:
            return 1
        for i in range(2,n+1):
            new=one+two
            one=two
            two=new
        return two
