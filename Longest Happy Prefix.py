class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lsp = [0] * n
        j = 0
        for i in range(1, n):
            while s[i] != s[j] and j > 0:
                j = lsp[j-1]
            if s[i] == s[j]:
                lsp[i] = j+1
                j += 1
        return s[:lsp[-1]]
