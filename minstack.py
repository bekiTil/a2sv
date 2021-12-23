class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack=[]
        self._min=[]
        

    def push(self, val: int) -> None:
        self._stack.append(val)
        if self._min:
            min=self._min[0]
            i=0
            while i<len(self._min):
                if val<self._min[i]:
                    self._min.insert(i,val)
                    break
                i+=1
            else:
                self._min.append(val)
             
        else:
            self._min.append(val)
            
       
       

    def pop(self) -> None:
        num=self._stack.pop()
        self._min.remove(num)
        return num
        

    def top(self) -> int:
        if self._stack:
            return self._stack[-1]
        

    def getMin(self) -> int:
        return self._min[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
