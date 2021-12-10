class Solution: 
    def select(self, arr, k):
        min=arr[k]
        num=k
        
        for i in range(k,len(arr)):
           
            if min>arr[i]:
                min=arr[i]
                num=i
        
        return min,num
                
            
        # code here 
    
    def selectionSort(self, arr,n):
        for i in range (n):
            min,num=self.select(arr,i)
            arr[num],arr[i]=arr[i],min
            
        return arr
