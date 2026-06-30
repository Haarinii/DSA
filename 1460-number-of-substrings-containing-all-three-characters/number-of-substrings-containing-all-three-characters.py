class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left=0
        cnt=0
        count={'a':0, 'b':0, 'c':0}
        for i in range(len(s)):
            count[s[i]]+=1
            while count['a']>0 and count['b']>0 and count['c']>0  :
                cnt+=len(s)-i
                count[s[left]]-=1
                left+=1
        return cnt
        