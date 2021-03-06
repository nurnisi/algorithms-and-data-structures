#884. Uncommon Words from Two Sentences
import collections

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        dict = {}
        for w in A.split() + B.split():
            if w in dict:
                dict[w] = dict[w] + 1
            else: 
                dict[w] = 1

        list = []
        for key, value in dict.items():
            if value == 1:
                list.append(key)

        return list

    def uncommonFromSentences2(self, A, B):
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1

        return [word for word in count if count[word] == 1]

    def uncommonFromSentences3(self, A, B):
        count = {}
        for word in A.split() + B.split():
            count[word] = count.get(word) + 1

        return [word for word in count if count[word] == 1]

    def uncommonFromSentences4(self, A, B):
        count = collections.Counter(A.split())
        count += collections.Counter(B.split())
        # or
        # count = collections.Counter(A.split() + B.split())

        return [word for word in count if count[word] == 1]

