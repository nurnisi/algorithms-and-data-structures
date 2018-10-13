# 860. Lemonade Change
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        five, ten = 0, 0
        for i in bills:
            if i == 5: five += 1
            elif i == 10 and five > 0:
                ten += 1
                five -= 1
            elif i == 20 and five > 0 and ten > 0:                
                five -= 1
                ten -= 1
            elif i == 20 and five >= 3:
                five -= 3
            else: return False

        return True

    def lemonadeChange2(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """ 
        five = ten = 0
        for bill in bills:
            if bill == 5: five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else: return False

        return True
