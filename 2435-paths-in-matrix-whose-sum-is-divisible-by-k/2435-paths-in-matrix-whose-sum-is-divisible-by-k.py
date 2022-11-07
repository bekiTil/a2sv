class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        
        n=len(grid)
        
        m=len(grid[0])
        
        dp=[[[0 for _ in range(k)] for _ in range(m)] for _ in range(n)]
        

                
        dp[0][0][grid[0][0]%k]=1
        for i in range(n):
            
            for j in range(m):
                
                for l in range(k):
                    temp=(l+grid[i][j])%k
                    if i-1>=0:
                        dp[i][j][temp]+=dp[i-1][j][l]
                    if j-1>=0:
                        dp[i][j][temp]+=dp[i][j-1][l]
                    dp[i][j][temp]%=((10**9)+7)
        
        return dp[n-1][m-1][0]
                    
                
                
                
        
        