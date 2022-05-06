class TrieNode:
    def __init__(self,value):
        self.children=[]
        self.value=value
        self.end=False
        self.suges=[]
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
        current=self.root
        
        for i in word:
            value=word
            current=current.findNode(i)
            if len(current.suges)==0:
                current.suges.append(word)
            else:
                k=0
                while k<len(current.suges):
                    if current.suges[k]>value:
                        current.suges[k],value=value,current.suges[k]
                    k+=1
                if len(current.suges)<3:
                    current.suges.append(value)
            
                    
                
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
    
    def suggest(self,word):
        current=self.root
        for i in word:
            current=current.findNode(i)
            if not current:
                return []
        return current.suges
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
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        new=Trie()
        for i in products:
            new.insert(i)
        preffix=""
        ans=[]
        for i in searchWord:
            preffix+=i
            ans.append(new.suggest(preffix))
        
        return ans
