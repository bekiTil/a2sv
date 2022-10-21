class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outDegree=defaultdict(int)
        level=deque([])
        back=defaultdict(list)
        for index,i in enumerate(graph):
            if len(i)==0:
                level.append(index)
            for val in i:
                back[val].append(index)
            outDegree[index]+=len(i)
        ans=[]
        while level:
            node=level.popleft()
            ans.append(node)
            for val in back[node]:
                outDegree[val]-=1
                if outDegree[val]==0:
                    level.append(val)
        # print(ans)
        ans.sort()
        return ans
            
        