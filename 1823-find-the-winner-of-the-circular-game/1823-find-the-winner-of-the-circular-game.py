class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [ i + 1 for i in range(n) ]
        person = 0
        while len(arr)>1:
            count = 1
            while count < k:
                count+=1
                person+=1
                person%=len(arr)
            arr.pop(person)
            person%=len(arr)
        return arr[0]
            
            
            