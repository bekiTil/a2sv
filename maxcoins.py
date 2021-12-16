    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i=0
        j=len(piles)-1
        new=0
        while j>i:
            new+=piles[j-1]
            i+=1
            j-=2
        return new
