class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        sett=set(nums)
        longest=1
        for i in sett:
            if i-1  not in sett:
                count=1
                x=i
                while x+1 in sett:
                    count+=1
                    x+=1
                longest= max(longest, count)
        return longest
        