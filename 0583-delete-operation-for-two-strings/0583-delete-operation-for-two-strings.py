class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
        
        for i in range(len(word2)):
            for j in range(len(word1)):
                if word2[i]==word1[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        print(dp[-1][-1])
        return abs(dp[-1][-1]-len(word1))+abs(dp[-1][-1]-len(word2))
        
        