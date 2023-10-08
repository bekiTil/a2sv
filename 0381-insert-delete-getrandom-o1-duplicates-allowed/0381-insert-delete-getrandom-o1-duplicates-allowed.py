class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.map = defaultdict(set)

    def insert(self, val: int) -> bool:
        res = len(self.map[val])
        self.map[val].add(len(self.arr))
        self.arr.append(val)
        return res==0
    
    def remove(self, val: int) -> bool:
        if len(self.map[val])>0:
            index = self.map[val].pop()
            self.arr[index] = self.arr[-1]
            if len(self.arr)-1 in self.map[self.arr[-1]]:
                self.map[self.arr[-1]].remove(len(self.arr)-1)
                self.map[self.arr[-1]].add(index)
            self.arr.pop()
            return True
        return False
            

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()