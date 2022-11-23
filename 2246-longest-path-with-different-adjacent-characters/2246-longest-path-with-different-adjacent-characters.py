class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph=defaultdict(list)
        for index,value in enumerate(parent[1:]):
            graph[value].append(index+1)
           
        
        print(graph)
        dp=[0 for _ in range(len(s))]
        def dfs(value):
            length1=0
            length2=0
            for val in graph[value]:
                if val not in visited:
                    visited.add(val)
                    depth=dfs(val)
                    if s[val]!=s[value]:
                        if depth>=length1:
                            length1,length2=depth,length1
                        elif depth>=length2:
                            length2=depth
           
            dp[value]=(length1+length2)+1
            return max(length1,length2)+1
        visited=set()
        visited.add(0)
        dfs(0)
       
        return max(dp)
            
                    