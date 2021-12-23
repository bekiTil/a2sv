class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        max=len(arr)
        ar=[]
        while max>0:
            new=arr.index(max)
            if new==max-1:
                max-=1
                continue
            elif new==0:
                i=0
                j=max-1
                while i<j:
                    arr[i],arr[j]=arr[j],arr[i]
                    i+=1
                    j-=1
                ar.append(max)
            else:
                i=0
                j=new
                while i<j:
                    arr[i],arr[j]=arr[j],arr[i]
                    i+=1
                    j-=1
                ar.append(new+1)
                i=0
                j=max-1
                while i<j:
                    arr[i],arr[j]=arr[j],arr[i]
                    i+=1
                    j-=1
                ar.append(max)
            max-=1
        return ar
