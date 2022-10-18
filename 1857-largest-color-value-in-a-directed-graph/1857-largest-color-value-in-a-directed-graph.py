class Solution:
    def largestPathValue(self, string: str, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        back=defaultdict(list)
        inDegree=defaultdict(int)
        n=len(string)
        dist=[[0 for _ in range(26)] for _ in range(n)]
        for x,y in edges:
            graph[x].append(y)
            back[y].append(x)
            inDegree[y]+=1
        level=deque([])
        for i in range(n):
            if not inDegree[i]:
                level.append(i)
        maxi=float("-inf")
        ans=0
        while level:
            node=level.popleft()
            for val in graph[node]:
                inDegree[val]-=1
                if not inDegree[val]:
                    level.append(val)

            for val in back[node]:
                for char in range(26):
                    if ord(string[node])-ord("a")==char:
                        dist[node][char]=max(dist[node][char],(dist[val][char]+1))
                    else:
                        dist[node][char]=max(dist[node][char],(dist[val][char]))
                    maxi=max(dist[node][char],maxi)
            if len(back[node])==0:
                char= ord(string[node])-ord("a")
                
                dist[node][char]+=1
                maxi=max(dist[node][char],maxi)
            ans+=1

        if ans==n:
            return maxi
        else:
            return -1