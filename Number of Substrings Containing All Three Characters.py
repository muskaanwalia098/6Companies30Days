class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        This function increments the counts based on the minimum 
        index between a, b, c. This is because after each all the 
        characters collectively form the minimum string from 0 to 
        the minimum index. If it cammot find the either a or b
        or c then it does not update the ans.
        """
        ans = 0
        idx_a, idx_b, idx_c = -1, -1, -1
        for i, n in enumerate(s):
            if n == 'a': idx_a = i
            elif n == 'b':  idx_b = i
            elif n == 'c':  idx_c = i

            if i > 1:
                ans += min(idx_a, idx_b, idx_c) + 1
        return ans
