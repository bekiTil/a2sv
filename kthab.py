class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(n):
            for i in range(len(n)):
                if n[i]==0:
                    n[i]=1
                else:
                    n[i]=0
            return n       
        def binary(n):
            if n==1:
                return [0]
            nw=binary(n-1)
            return nw+[1] + list(reversed(invert(nw)))
        return str(binary(n)[k-1])
