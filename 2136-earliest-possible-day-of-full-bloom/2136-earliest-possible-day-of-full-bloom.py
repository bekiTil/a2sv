class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        res = 0
        solution=0
        temp=[]
        for i in range(len(plantTime)):
            temp.append((growTime[i],plantTime[i]))
        temp.sort()
        for i,j in temp:
            solution = max(solution, i) + j
        return solution
        