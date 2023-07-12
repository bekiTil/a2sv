class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        for i in range(31):
            if 2 ** i & left and 2 ** i & right and (right -left) + 1 <= 2 **i:
                ans += 1<<i
        return ans