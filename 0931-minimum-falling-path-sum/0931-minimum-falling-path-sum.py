class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp=[[float("inf") for _ in range(len(matrix[0])+2) ] for _ in range(len(matrix)+1)]
        
        
        n=len(matrix)-1
        
        for i in range(len(dp[-1])):
            dp[-1][i]=0
        for i in dp:
            print(*i)
        for i in range(n,-1,-1):
            for j in range(1,n+2):
                dp[i][j]=min(dp[i+1][j],dp[i+1][j+1],dp[i+1][j-1])+matrix[i][j-1]
        for i in dp:
            print(*i)
        return min(dp[0][1:n+2])
        