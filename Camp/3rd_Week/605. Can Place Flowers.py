class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=0
        new_flower=0
        if len(flowerbed)==1:
            if flowerbed[i]==0:
                return new_flower+1>=n
            else:
                return new_flower==n
        while i<len(flowerbed):
            if flowerbed[i]==0:
                if i==0 and flowerbed[i+1]==0:
                    new_flower+=1
                    flowerbed[i]=1
                elif i==len(flowerbed)-1 and flowerbed[i-1]==0:
                    new_flower+=1
                    flowerbed[i]=1
                elif flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    new_flower+=1
                    flowerbed[i]=1
            i+=1
        return new_flower>=n
                    
                    
                    
