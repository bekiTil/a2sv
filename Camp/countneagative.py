class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        new=len(grid[0])-1
        n=0
        m=len(grid[0])-1
        for k in grid:
            i=0
            j=new
            while i<=j:
                mid=(i+j)//2
                if k[mid]<0:
                    m=mid
                    j=mid-1
                    
                else:
                    i=mid+1
            if m==len(k)-1 and k[-1]>=0:
                n+=(len(k)-(m+1))
            else:
                if m==0 and k[m]>0:
                    n+=(len(k)-m-1)
                else:
                    n+=(len(k)-m)
            new=mid
        return n
