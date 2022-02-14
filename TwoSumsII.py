class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first=0
        last=len(numbers)-1
        arr=[]
        while first<last:
            if (numbers[last]+numbers[first])==target:
                arr.append(first+1)
                arr.append(last+1)
                return arr
            elif (numbers[last]+numbers[first])>target:
                last-=1
                continue
            else:
                first+=1
                continue
