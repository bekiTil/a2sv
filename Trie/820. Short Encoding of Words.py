class TrieNode:
    def __init__(self,value):
        self.children=[]
        self.value=value
        self.end=False
        self.suffix=set()
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
        
        for i in range(len(word)):
            che=word[i:]
            if che not in self.root.suffix:
                self.root.suffix.add(word[i:])
            else:
                break
        
        
    def suffixs(self,word):
        if word not in self.root.suffix:
            return False
        return True
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
    def minimumLengthEncoding(self, words: List[str]) -> int:
        new=[]
        for i in words:
            heappush(new,(-1*len(i),i))
        print(new)
        node=Trie()
        ans=0
        
        while new:
            i=heappop(new)
            
            if not node.suffixs(i[1]):
                ans+=(-1*i[0])
                ans+=1
                node.insert(i[1])
        return ans
                
                
