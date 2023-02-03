class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1==p2==p3==p4:  return False
        def distance(pt1, pt2):
            return math.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
        sides = [
            distance(p1, p2),
            distance(p1, p3),
            distance(p1, p4),
            distance(p2, p3),
            distance(p2, p4),
            distance(p3, p4),
        ]
        sides.sort()
        if sides[0] == sides[1] == sides[2] == sides[3]:
            if sides[4] == sides[5]:    return True
        return False
