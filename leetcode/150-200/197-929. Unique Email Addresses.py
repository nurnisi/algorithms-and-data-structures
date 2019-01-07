# 929. Unique Email Addresses
class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        s = set()
        for e in emails:
            sp = e.split('@')
            fin = ''.join(sp[0].split('.')).split('+')[0] + '@' + sp[1]
            s.add(fin)
        return len(s)

sol = Solution()
print(sol.numUniqueEmails(["test.emailalex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))