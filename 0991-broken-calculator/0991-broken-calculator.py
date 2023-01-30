class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count=0
        if startValue>target:
            return abs(startValue-target)
        while startValue>target or startValue<target:
            if target%2==0 and target>startValue:
                target//=2
            else:
                target+=1
            count+=1
        return count
    