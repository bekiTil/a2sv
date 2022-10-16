class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        self.val=len(parents)
        graph=defaultdict(list)
        temp=[0]*self.val
        for index,i in enumerate(parents):
            if i!=-1:
                graph[i].append(index)
        visited=set()
        def dfs(node):
            memo=[-1,-1]
            for val in graph[node]:
                if val not in visited:
                    ans=dfs(val)
                    if memo[0]==-1:
                        memo[0]=ans
                    else:
                        memo[1]=ans
                    visited.add(val)
            if node==0:
                if memo[0]==-1:
                    return 1
                elif memo[1]==-1:
                    temp[node]=memo[0]
                    return memo[0]+1
                else:
                    temp[node]=memo[0]*memo[1]
                    return sum(memo)+1
                    
            if memo[0]==-1:
                temp[node]=self.val-1
                return 1
            elif memo[1]==-1:
                temp[node]=(self.val-memo[0]-1)*memo[0]
                
                return memo[0]+1
            else:
                
                temp[node]=(self.val-sum(memo)-1)*memo[0]*memo[1]
                return sum(memo)+1
        visited.add(0)
        dfs(0)
        return temp.count(max(temp))