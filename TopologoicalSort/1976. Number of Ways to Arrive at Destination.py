class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(list)
        for i in roads:
            city1,city2,weight=i
            graph[city1].append((city2,weight))
            graph[city2].append((city1,weight))
        final=[[float(inf),1] for _ in range(n)]
        final[0][0]=0
       
        new=[]
        heapq.heappush(new,(0,0))
        visited=set()
        while new:
            node=heapq.heappop(new)
            if node not in visited:
                visited.add(node[1])
                for n,w in graph[node[1]]:
                    if final[n][0]==node[0]+w:
                        final[n][1]+=final[node[1]][1]
                    if final[n][0]> node[0] + w:
                        final[n][0]=final[node[1]][0]+w
                        final[n][1]=final[node[1]][1]
                        heapq.heappush(new,(final[n][0],n))
                    
                    
                    
       
        return final[-1][1]%(10**9+7)
        # final=[[0,float(-inf)] for i in range(n)]
        # final=
        # nodes=set()
        
