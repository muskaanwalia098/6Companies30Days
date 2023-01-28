class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        bucket = [0]*10

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                bucket[int(s)] += 1
                bucket[int(g)] -= 1
        
        cows = len(secret) - bulls
        for b in bucket:
            cows -= max(0, b)

        return (f'{bulls}A{cows}B')
