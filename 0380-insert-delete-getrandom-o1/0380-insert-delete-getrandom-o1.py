class RandomizedSet:

    def __init__(self):
        self.list=[]
        self.dict=defaultdict(int)
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val]=len(self.list)
        
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.dict:
            index=self.dict[val]
            self.list[index] , self.list[-1]=self.list[-1],self.list[index]
            self.list.pop()
            if len(self.list)>index:
                self.dict[self.list[index]]=index
            del self.dict[val]
            return  True
        return False

    def getRandom(self) -> int:
        return choice(self.list)
        