class DetectSquares:

    def __init__(self):
        self.store = collections.Counter()

    def add(self, point: List[int]) -> None:
        self.store[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0
        
        for i, j in self.store:
            if abs(x-i)!=abs(y-j) or x==i or y==j: continue
            ans += self.store[(i, j)]*self.store[(i, y)]*self.store[(x, j)]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)