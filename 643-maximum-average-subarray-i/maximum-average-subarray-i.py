class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total=sum(nums[:k])
        max_val=total
        for i in range(k,len(nums)):
            total+=nums[i]
            total-=nums[i-k]
            max_val=max(total, max_val)
        return max_val/k

        