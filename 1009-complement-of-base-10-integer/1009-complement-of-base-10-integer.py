class Solution:
    def bitwiseComplement(self, num: int) -> int:
        for i in range(31,-1,-1):
            if num & (1 << i):
                break

        for x in range(i,-1,-1):
            num^=(1 << x)
        return num