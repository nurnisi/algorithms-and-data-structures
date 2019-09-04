# 380. Insert Delete GetRandom O(1)
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.set:
            return False
        self.set.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.set:
            self.set.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return list(self.set)[random.randint(0, len(self.set)-1)]
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()