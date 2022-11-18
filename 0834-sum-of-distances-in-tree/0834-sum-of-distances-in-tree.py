class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        dp=[[0,0] for _ in range(n)]
        ans=[0 for _ in range(n)]
        
        tree=defaultdict(list)
        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
        
     
        def dfs(node,parent):
            total=0
            temp=0
            for val in tree[node]:  
                if val != parent:
                    value=dfs(val,node)
                    total+=(value[0]+value[1])
                    temp+=value[1]
            dp[node][0],dp[node][1]=total,temp+1
            return total,temp+1
       
        dfs(0,-1)
        
     
        
        def dfs2(node,parent):
            for val in tree[node]:
                if val!=parent:
                    dp[val][0]+=(dp[node][0]-(dp[val][0]+dp[val][1])+(dp[node][1]-dp[val][1]))
                    dp[val][1]=dp[node][1]
                    ans[val]=dp[val][0]
                    dfs2(val,node)
        dfs2(0,-1)
        ans[0]=dp[0][0]
        return ans
                    
                