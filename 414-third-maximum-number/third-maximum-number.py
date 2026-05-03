class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_num=[]
        for i in nums:
            if i not in sorted_num:
                sorted_num.append(i)
        sorted_num=sorted(sorted_num)
        if len(sorted_num)>=3:
            return sorted_num[-3]
        return sorted_num[-1]