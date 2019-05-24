# 836. Rectangle Overlap
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        return not (rec1[2] <= rec2[0] or # left
                    rec1[3] <= rec2[1] or # bottom
                    rec1[0] >= rec2[2] or # right
                    rec1[1] >= rec2[3])   # top

    def isRectangleOverlap2(self, rec1, rec2):
        def intersect(p_xy1, p_xy2, q_xy1, q_xy2):
            return min(p_xy2, q_xy2) > max(p_xy1, q_xy1)

        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and # width
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))    # height
        