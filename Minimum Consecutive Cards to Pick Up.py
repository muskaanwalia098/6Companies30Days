class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hmap = {}
        min_len = float("inf")
        for i,n in enumerate(cards):
            if n in hmap:
                min_len = min(min_len, (i - hmap[n] + 1))
            hmap[n] = i
        return -1 if min_len == float("inf") else min_len
