class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, stack, target):
            if len(stack) == k:
                if target == 0:
                    result.append(stack.copy())
                return

            for x in range(start+1, 10):
                stack.append(x)
                backtrack(x, stack, target-x)
                stack.pop()

        backtrack(0, [], n)
        return result
