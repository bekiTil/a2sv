class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        new={}
        doubled=[]
        for i in changed:
            if len(new)==len(doubled):
                if i/2 in new.keys() and new[i/2]>0:
                    doubled.append(i//2)
                    new[i/2]-=1
                else:
                    if i in new.keys():
                        new[i]+=1
                    else:
                        new[i]=1
            else:
                if i/2 in new.keys() and new[i/2]>0:
                    doubled.append(i//2)
                    new[i/2]-=1
                elif i in new:
                    new[i]+=1
                else:
                    new[i]=1
        if len(doubled)==len(changed)/2:
    
            return doubled
        else:
           
            return []
