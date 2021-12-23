class MyCircularDeque:

    def __init__(self, k: int):
        self.deque=[]
        self.front=0
        self.back=0
        self.len=k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.deque.insert(0,value)
            self.back+=1
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.deque.append(value)
            self.back+=1
            return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.deque.pop(0)
            self.back-=1
            return True
            

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.deque.pop()
            self.back-=1
            return True
            

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.back-1]
        return self.deque[self.back]

    def isEmpty(self) -> bool:
        return self.front==self.back 
        

    def isFull(self) -> bool:
        return self.back - self.front==self.len
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
