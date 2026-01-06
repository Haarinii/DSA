class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st={}
        ts={}
        for i in range(len(s)):
            s1=s[i]
            t1=t[i]
            if s1 in st:
                if st[s1]!=t1:
                    return False
            else:
                st[s1]=t1
            if t1 in ts:
                if ts[t1]!=s1:
                    return False
            else:
                ts[t1]=s1
        return True
        