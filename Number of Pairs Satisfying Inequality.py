class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        q = []
        ans = 0
        n = len(nums1)

        for i in reversed(range(n)):
            current = nums1[i] - nums2[i] - diff
            # location = bisect.bisect_left(q, current)
            # ans += len(q) - location
            ans += len(q) - bisect.bisect_left(q, current)
            bisect.insort(q, current + diff)
        return ans
