# 341. Flatten Nested List Iterator
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """

#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """

#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator2(object):

    def __init__(self, nestedList):
        self.array = []
        self.process(nestedList)
        self.i = 0
        
    def process(self, nl):
        for x in nl:
            if x.isInteger(): 
                self.array.append(x.getInteger())
            else: 
                self.process(x.getList())

    def next(self):
        self.i += 1
        return self.array[self.i - 1]

    def hasNext(self):
        return self.i < len(self.array)

class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self):
        self.hasNext()
        nl, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nl[i].getInteger()

    def hasNext(self):
        s = self.stack
        while s:
            nl, i = s[-1]
            if i == len(nl):
                s.pop()
            else:
                x = nl[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False

# Your NestedIterator object will be instantiated and called as such:
i, v = NestedIterator([[1,1],2,[1,1]]), []
while i.hasNext(): v.append(i.next())
print(v)