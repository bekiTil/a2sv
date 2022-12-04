class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(node,arr,target):
            if node==target:
                ans.append(arr)
                return 
            for val in graph[node]:
                new=deepcopy(arr)
                new.append(val)
                dfs(val,new,target)
                
        ans=[]
        dfs(0,[0],len(graph)-1)
        # print(ans)
        return ans