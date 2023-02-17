class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper( current, opened, closed, n):
            if n == 0:
                return []
            if opened == closed == n:
                return [current]
            o, c = [],[]
            out = []
            if opened < n:
                o = helper(current + '(', opened + 1, closed, n)
            if opened > closed:
                c = helper(current + ')', opened, closed + 1, n)
            return o + c
        return helper('', 0, 0, n)
        
   
        
        