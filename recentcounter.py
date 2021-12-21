class RecentCounter:

    def __init__(self):
        self.stack=[]
        self.queue=[]
      
        
        

    def ping(self, t: int) -> int:
        self.stack.append(t)
        self.queue.append(t)
        
        while self.queue[0] not in range(t-3000,t+1):
            self.queue.pop(0)
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
