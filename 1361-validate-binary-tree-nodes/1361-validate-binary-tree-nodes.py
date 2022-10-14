class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        self.ans=0
        visited=set()
        graph=defaultdict(int)
        for i in range(len(leftChild)):
            if leftChild[i]!=-1:
                graph[leftChild[i]]+=1
            if rightChild[i]!=-1:
                graph[rightChild[i]]+=1
        ans=0
        temp=-1
        for i in range(n):
            if graph[i]==0:
                temp=i
                ans+=1
        if ans>1:
            return False
        if temp==-1:
            return False
        def dfs(node):
            level=[node]
            while level:
                value=level.pop()
                if leftChild[value] not in visited :
                    if  leftChild[value]!=-1:
                        level.append(leftChild[value])
                        self.ans+=1
                        visited.add(leftChild[value])
                else:
                    return False
                if rightChild[value] not in visited :
                    if rightChild[value]!=-1:
                        level.append(rightChild[value])
                        self.ans+=1
                        visited.add(rightChild[value])
                else:
                    return False
            return True
        visited.add(temp)
        value=dfs(temp)
        return value and (self.ans==n-1)