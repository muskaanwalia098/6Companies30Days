class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        result = 1
        for i in range(len(points)):
            pt1 = points[i]
            count_slopes = defaultdict(int)
            for j in range(i+1, len(points)):
                pt2 = points[j]
                if pt1[0] == pt2[0]:
                    slope = float("inf")
                else:
                    slope = ((pt2[1] - pt1[1]) / (pt2[0] - pt1[0]))
                count_slopes[slope] += 1
                result = max(result, count_slopes[slope] + 1)
        return result
