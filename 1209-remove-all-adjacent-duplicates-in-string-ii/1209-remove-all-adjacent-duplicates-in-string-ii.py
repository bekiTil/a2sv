class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        arr=[]
        for i in s:
            temp=False
            while arr and arr[-1][0]==i and (temp or arr[-1][-1]>=k-1):
                temp=True
                arr.pop()
            if not temp:
                if arr and arr[-1][0]==i:
                    arr.append((i,arr[-1][-1]+1))
                else:
                    arr.append((i,1))
        return "".join(char for char,num in arr)
                    
            
                