class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        store={}
        def helper(index):
            if index>=len(questions):
                return 0
            elif index in store:
                return store[index]
            else:
                hold=questions[index][0]+helper(index+questions[index][1]+1)
                left=helper(index+1)
                memo=max(hold,left)
                store[index]=memo
                return memo
                
        return helper(0)
           
