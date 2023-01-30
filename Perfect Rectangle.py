class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corners = set()

        for x1, y1, x2, y2 in rectangles:
            bottom_left = (x1, y1)
            upper_left = (x1, y2)
            bottom_right = (x2, y1)
            upper_right = (x2, y2)
            area += ((y2 - y1) * (x2 - x1))
            for i in [bottom_left, upper_left, bottom_right, upper_right]:
                if i not in corners:    corners.add(i)
                else:   corners.remove(i)

        if len(corners) != 4:   return False

        corners = sorted(corners)
        left_bottom = corners.pop(0)
        right_upper = corners.pop()
        return area == ((left_bottom[0] - right_upper[0]) * (left_bottom[1] - right_upper[1]))
