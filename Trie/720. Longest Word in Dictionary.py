class TrieNode:
    def __init__(self,value):
        self.children=[]
        self.value=value
        self.end=False
    def findNode(self,value):
        for i in self.children:
            if i.value==value:
                return i
        return None
        
class Trie:

    def __init__(self):
        self.root=TrieNode(None)

    def insert(self, word: str) -> None:
        current=self.root
        for i in word:
            node =current.findNode(i)
            if not node:
                new=TrieNode(i)
                current.children.append(new)
                current=new
            else:
                current=node
        current.end=True
            
    def search(self, word: str) -> bool:
        current=self.root
        for i in word:
            node=current.findNode(i)
            if node:
                current=node
            else:
                return False
        if current.end:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        current=self.root
        for i in prefix:
            node=current.findNode(i)
            if node:
                current=node
            else:
                return False
        return True
class Solution:
    def longestWord(self, words: List[str]) -> str:
        length=[]
        node=Trie()
        for i in words:
            heappush(length,(len(i),i))
        print(length)
        ans=""
        while length:
            key,new=heappop(length)
            if len(new)-1!=0:
                if node.startsWith(new[:-1]):
                    if len(ans)<len(new):
                        ans=new
                        node.insert(new)
                    else:
                        if ans>new:
                            ans=new
                        node.insert(new)

            else:
                if len(ans)==0:
                    ans=new
                    node.insert(new)
                else:
                    if ans[-1]>new[-1]:
                        ans=new
                    node.insert(new)
            
        return ans
                
