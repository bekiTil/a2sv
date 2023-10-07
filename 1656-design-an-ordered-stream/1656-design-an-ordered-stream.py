class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None for i in range(n)]
        self.index = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1]= value
        previous = self.index
        while self.index <len(self.arr) and self.arr[self.index]:
            self.index+=1
        if previous == self.index:
            return []
        return self.arr[previous:self.index]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)