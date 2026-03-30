class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cs = dict()
        ct = dict()
        for ps,pt in zip(s, t):
            cs[ps] = cs.get(ps, 0) + 1
            ct[pt] = ct.get(pt, 0) + 1
            
        return ct == cs