class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.recent = deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.recent.remove(key)
            self.recent.appendleft(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.recent.remove(key)
        self.recent.appendleft(key)
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            not_used = self.recent.pop()
            del self.cache[not_used]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)