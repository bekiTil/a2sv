class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        val =0
        for i in derived:
            val = val ^ i
        return val ==0