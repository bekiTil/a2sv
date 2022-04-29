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
        
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
