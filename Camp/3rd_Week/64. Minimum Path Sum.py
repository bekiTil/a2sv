class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo={}
        def path(m,n):
            if (m,n) in memo:
                return memo[(m,n)]
            if m==len(grid)-1 and n==len(grid[0])-1:
                return grid[m][n] 
            elif m==len(grid)-1:
                return sum(grid[m][n:])
            elif n==len(grid[0])-1:
                l=0
                for x in range(m,len(grid)):
                    l+=grid[x][n]
                return l
            else:
                down=grid[m][n]+path(m+1,n)
                right=grid[m][n]+path(m,n+1)
                memo[(m,n)]=min(down,right)
                return min(down,right)
        
        return path(0,0)
                    
 class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[float("inf") for _ in range(len(grid[0])+1) ]for j in range(len(grid)+1)]
        dp[len(grid)][len(grid[0])-1]=0
        for i in range(len(dp)-2,-1,-1):
            for j in range(len(dp[0])-2,-1,-1):
                dp[i][j]=min(grid[i][j]+dp[i+1][j],grid[i][j]+dp[i][j+1])
        return dp[0][0]
