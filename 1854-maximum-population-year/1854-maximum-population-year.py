class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        ans=[1950,0]
        for i in range(1950,2050):
            temp=0
            # print(i)
            for j in logs:
                if j[1]>i and j[0]<=i:
                    temp+=1
            if temp>ans[1]:
                ans=[i,temp]
        return ans[0]
                    