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
        word=word.split("/")[1:]
        
        for i in word:
            
            node =current.findNode(i)
            
            if not node:
                new=TrieNode(i)
                current.children.append(new)
                current=new
            else:
                current=node
            
       
        current.end=True
    def folder(self,word):
        word=word.split("/")[1:]
        current=self.root
        
        for i in word:
            node=current.findNode(i)
            if not node:
                return False
            if node.end:
                return True
            current=node
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
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        new=Trie()
        hea=[]
        for i in folder:
            hea.append((len(i),i))
        hea.sort()
       
        ans=[]
        for i in hea:
            if not new.folder(i[1]):
                ans.append(i[1])
                new.insert(i[1])
       
        return ans
