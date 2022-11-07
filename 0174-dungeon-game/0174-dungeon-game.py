class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp=[[float("inf") for _ in range(len(dungeon[0])+1)] for _ in range(len(dungeon)+1)]
        
        dp[len(dungeon)][len(dungeon[0])-1]=1
        dp[len(dungeon)-1][len(dungeon[0])]=1
        
        for i in range(len(dungeon)-1,-1,-1):
            
            for j in range(len(dungeon[0])-1,-1,-1):
                
                dp[i][j]=max(1,min(dp[i+1][j],dp[i][j+1])-dungeon[i][j])
            
        # for i in dp:
        #     print(*i)
        return dp[0][0]