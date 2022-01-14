  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic={}
        stack=[]
        j=0
        for i in range(len(position)):
            dic[position[i]]=speed[i]
        
        new=sorted(dic.items())
       
        for i in range(len(new)-1,-1,-1):
            stack.append((target-new[i][0])/new[i][1])
        max=0
        for i in stack:
            if max<i:
                max=i
                j+=1
        return j
                
