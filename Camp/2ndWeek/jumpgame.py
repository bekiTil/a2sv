class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        index=deque([start])
        visited=set()
        if arr[start]==0:
            return True
        while index:
            length=len(index)
            for i in range(length):
                new=index.pop()
                visited.add(new)
                for j in [new+arr[new],new-arr[new]]:
                    if 0<=j<len(arr) and j not in visited:
                        index.append(j)
                        visited.add(new)
                        if arr[j]==0:
                            return True
        return False
                        
    
