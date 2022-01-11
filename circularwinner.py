class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        new=list(range(1,n+1))
        def min(n,k,pointer):
            if len(n)==1:
                return n[0]
            else:
                if k>len(n):
                    if k+pointer>=2*len(n):
                        n.pop(((pointer+k-len(n))-1)%len(n))
                        if (((pointer+k-(len(n)+1))-1)%(len(n)+1))==len(n):
                            pointer=0
                        else:
                            pointer=((pointer+k-(len(n)+1))-1)%(len(n)+1)
                    else:
                        n.pop((pointer+k-len(n))-1)
                        if (pointer+k-(len(n)+1))-1==len(n):
                            pointer=0
                        else:
                            pointer=(pointer+k-(len(n)+1))-1
                else: 
                    if pointer+k-1>len(n)-1:
                        n.pop((k+pointer-1)-len(n))
                        if ((k+pointer-1)-(len(n)+1))==len(n):
                            pointer=0
                        else:
                            pointer=(k+pointer-1)-(len(n)+1)
                    else:
                        n.pop(k+pointer-1)
                        if ((k+pointer-1))==len(n):
                            pointer=0
                        else:
                            pointer=k+pointer-1
               
                return min(n,k,pointer)
 
        return min(new,k,0)
        
