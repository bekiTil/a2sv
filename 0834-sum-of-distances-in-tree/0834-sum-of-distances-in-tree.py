class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        dp=[[0,0] for _ in range(n)]
        
        tree=defaultdict(list)
        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
        
        visited=set()
        def dfs(node):
            total=0
            temp=0
            for val in tree[node]:  
                if val not in visited:
                    visited.add(val)
                    value=dfs(val)
                    total+=(value[0]+value[1])
                    temp+=value[1]
            dp[node][0],dp[node][1]=total,temp+1
          
            return total,temp+1
        visited.add(0)
        dfs(0)
        
     
        
        def dfs2(node):
            for val in tree[node]:
                if val not in visited:
                    dp[val][0]+=(dp[node][0]-(dp[val][0]+dp[val][1])+(dp[node][1]-dp[val][1]))
                    dp[val][1]=dp[node][1]
                    visited.add(val)
                    dfs2(val)
        visited=set()
        visited.add(0)
        dfs2(0)
      
        ans=[]
        for i,j in dp:
            ans.append(i)
        return ans
                    
                    
                