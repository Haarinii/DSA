class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        hashtab=[-1]*256
        left=maxlen=0
        for right in range(n):
            if hashtab[ord(s[right])]!=-1:
                left=max(hashtab[ord(s[right])]+1,left)
            length=right-left+1
            maxlen=max(maxlen, length)
            hashtab[ord(s[right])]=right
        return maxlen