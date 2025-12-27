class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter=set()
        for i in nums2:
            if i in nums1:
                inter.add(i)
        return list(inter)