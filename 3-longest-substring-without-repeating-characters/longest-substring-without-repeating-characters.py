class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str=[]
        maxx=0
        for i in s:
            while i in sub_str:
                sub_str.pop(0)
            sub_str.append(i)
            maxx=max(maxx, len(sub_str))
        return maxx