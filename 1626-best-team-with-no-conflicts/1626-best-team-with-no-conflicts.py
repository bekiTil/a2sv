class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        temp=[]
        for i in range(len(scores)):
            temp.append((ages[i],scores[i]))
        temp.sort()
        dp=[0]*len(scores)
        print(temp)
        for i in range(len(scores)):
            dp[i] = temp[i][1]
            for j in range(i):
                if temp[i][1] >= temp[j][1]:
                    dp[i] = max(dp[i], temp[i][1] + dp[j])
        print(dp)
        return max(dp)