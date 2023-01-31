class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # [2,6,4,8,10,9,15]
        # [2,4,6,8,9,10,15]
        N = len(nums)
        if N == 1:
            return 0
        
        i, j = 0, N-1

        while i < N-1 and nums[i] <= nums[i+1]:
            i += 1
        while j > 0 and nums[j] >= nums[j-1]:
            j -= 1
        if i > j:   return 0

        # need to run another set of loop to find lower bound and upper bound
        # for example [1, 3, 7, 2, 5, 4, 6, 10]
        # after 1st round, i = 2, j = 5
        # but it's wrong as the values 3 and 6 will not be included in sort

        temp = nums[i : j+1]
        tempMin, tempMax = min(temp), max(temp)

        # run a the loops in opposite direction to increase the bound
        while i > 0 and tempMin < nums[i-1]:
            i -= 1
        while j < N-1 and tempMax > nums[j+1]:
            j += 1
        return j - i + 1

        # nums2 = sorted(nums)
        # N = len(nums)
        # l, r = N, 0
        # for i in range(len(nums)):
        #     if nums[i] != nums2[i]:
        #         l = min(l, i)
        #         r = max(r, i)
        # if l == N:  return 0
        # return r - l + 1
