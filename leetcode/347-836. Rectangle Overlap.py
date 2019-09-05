# 836. Rectangle Overlap
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[2] <= rec2[0] or # left
                    rec1[3] <= rec2[1] or # bottom
                    rec1[0] >= rec2[2] or # right
                    rec1[1] >= rec2[3])   # top