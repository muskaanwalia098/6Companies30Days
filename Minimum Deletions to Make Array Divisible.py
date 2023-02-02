class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gcdN = gcd(*numsDivide)
        small = float("inf")
        for num in nums:
            if gcdN % num == 0:
                small = min(small, num)
        ans = 0
        if small == float("inf"):
            return -1
        for num in nums:
            if num < small:
                ans += 1
        return ans
