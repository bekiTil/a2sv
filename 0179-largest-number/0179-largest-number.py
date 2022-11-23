class Solution:
    def largestNumber(self, array: List[int]) -> str:
       
        for i in range(1,len(array)):
            j=0
            temp=str(array[i])
            while j<i:
                print(j,i,temp)
                if temp+str(array[j])>str(array[j])+temp:
                    array[j],array[i]=int(temp),array[j]
                    
                    temp=str(array[i])
                    print(temp)
        
                j+=1
        ans=[]
        
        for i in array:
            ans.append(str(i))
        if array[0]==0:
            return "0"
        return "".join(ans)