class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for point in points:
            pointMap = {}
            for secondPoint in points:
                if point == secondPoint:
                    continue
                distance = ((point[0]-secondPoint[0])*(point[0]-secondPoint[0]) + 
                (point[1]-secondPoint[1])*(point[1]-secondPoint[1]))
                if distance not in pointMap:
                    pointMap[distance] = 0
                pointMap[distance] += 1

            for value in pointMap.values():
                if value >= 2:  count += value * (value - 1)
            pointMap.clear()
        return count
