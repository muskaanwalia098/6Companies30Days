class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counts = collections.Counter(nums)
        vacancy = defaultdict(int)

        for num in nums:
            if counts[num]:
                counts[num] -= 1
                if vacancy[num-1]:
                    vacancy[num-1] -= 1
                    vacancy[num] += 1
                elif counts[num+1] and counts[num+2]:
                    counts[num+1] -= 1
                    counts[num+2] -= 1
                    vacancy[num+2] += 1
                else:
                    return False
        return True
