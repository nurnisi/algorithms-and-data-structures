# 929. Unique Email Addresses
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for em in emails:
            loc, dom = em.split('@')
            loc = ''.join(loc.split('+')[0].split('.'))
            s.add(loc + '@' + dom)
        return len(s)