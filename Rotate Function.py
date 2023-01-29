class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s = sum(nums) # Sum of the array
        result = val = sum(ele * idx for idx, ele in enumerate(nums))

        for pivot in range(len(nums)-1, -1, -1):
            """
            Can be used to only update the result already calculated. 
            When we subtract F(1) from F(0), I found that if we add
            the sum of the array nums to F(0) and subtract only the 
            pivot * len(nums), it ends up giving the exact same answer.
            """
            val = val + s - len(nums)*nums[pivot]
            result = max(result, val)

        return result
