class MyQueue:

    def __init__(self):
        self._stack=[]
        self._stacks=[]
        self.top=None

    def push(self, x: int) -> None:
        if not self._stack:
            self.top=x
        self._stack.append(x)
        

    def pop(self) -> int:
        
        if not self._stacks:
            while self._stack:
                self._stacks.append(self._stack.pop())
        return self._stacks.pop()
        

    def peek(self) -> int:
        if not self._stacks:
            return self.top
        return self._stacks[-1]
        

    def empty(self) -> bool:
        return not self._stack and not self._stacks
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
