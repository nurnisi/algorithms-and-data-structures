# 49. Group Anagrams
import collections
class Solution:
    # TLE: 100/101 test passed
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

    # Accepted O(n^2logn)
    def groupAnagrams2(self, strs):
        d, ans = {}, []
        for s in strs:
            srt = ''.join(sorted(s))
            if srt in d:
                ans[d[srt]].append(s)
            else:
                d[srt] = len(ans)
                ans.append([s])
        
        return ans
 
    # leetcode solution
    def groupAnagrams3(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())

sol = Solution()
print(sol.groupAnagrams3(["eat", "tea", "tan", "ate", "nat", "bat"]))