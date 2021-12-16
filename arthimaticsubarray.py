def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n=[]
        for i in range(len(l)):
            new=sorted(nums[l[i]:r[i]+1] ,reverse=True)
            dif=new[0]-new[1]
           
            for i in range(1,len(new)-1):
                if dif!=new[i]-new[i+1]:
                    n.append(0==1)
                    break
            else:
                n.append('true')
        
        return n
        
