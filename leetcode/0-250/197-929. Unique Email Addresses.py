# 929. Unique Email Addresses
class Solution:
    def numUniqueEmails(self, emails):
        s = set()
        for e in emails:
            sp = e.split('@')
            fin = ''.join(sp[0].split('.')).split('+')[0] + '@' + sp[1]
            s.add(fin)
        return len(s)

    def numUniqueEmails2(self, emails):
        seen = set()
        for e in emails:
            seen.add(''.join(e.split('@')[0].split('.')).split('+')[0] + '@' + e.split('@')[1])
        return len(seen)

    def numUniqueEmails3(self, emails):
        seen = set()
        for e in emails:
            local, domain = e.split('@')
            if '+' in local: local = local[:local.index('+')]
            seen.add(local.replace('.', '') + '@' + domain)
        return len(seen)

sol = Solution()
print(sol.numUniqueEmails2(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))