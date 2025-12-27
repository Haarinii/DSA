class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        frq={}
        for i in nums:
            frq[i]=frq.get(i,0)+1
        for i in frq:
            if frq[i]>n//2:
                return i