# 49. Group Anagrams
# TLE: 100/101 test passed
import collections
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        count = []
        for s in strs:
            count.append(collections.Counter(s))

        elements = [i for i in range(len(count))]
        ans = []
        while elements:
            index = elements[0]
            anagrams, temp, s = [strs[index]], [], count[index]
            for i in elements[1:]:
                if s == count[i]:
                    anagrams.append(strs[i])
                else:
                    temp.append(i)
            elements = temp
            ans.append(anagrams)
        
        return ans
 
sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))