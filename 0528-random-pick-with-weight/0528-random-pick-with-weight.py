class Solution:
    def __init__(self, w: List[int]):
        total= sum(w)
        self.weight = [w[0]/total]
        for i in range(1, len(w)):            
            self.weight.append(self.weight[-1]+w[i]/total)

    def pickIndex(self) -> int:
        left, right= 0, len(self.weight)-1
        number = random.random()
        while left < right:
            mid = (left+right)//2
            if self.weight[mid] <= number:
                left = mid+1
            else: 
                right = mid
        return left
