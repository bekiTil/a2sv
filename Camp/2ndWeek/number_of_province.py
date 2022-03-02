class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        number_of_province=0
        upcoming=[0]*len(isConnected)
        def dfs(node):
            upcoming[node]=1
            for i in range(len(isConnected)):
                if isConnected[node][i] and not upcoming[i]:
                    dfs(i)
        for i in range(len(isConnected)):
            if not upcoming[i]:
                number_of_province+=1
                dfs(i)
        return number_of_province
            
