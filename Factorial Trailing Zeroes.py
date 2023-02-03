class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans, p = 0, 5
        while((n//p)>0):
            ans += n//p
            p *= 5
        return ans
