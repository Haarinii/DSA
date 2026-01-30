class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        st=0
        count=0
        max_1=0
        for i in range(len(nums)):
            if(nums[i]==0):
                count+=1
            while count >k:
                if nums[st]==0:
                    count-=1
                st+=1
            max_1= max(max_1, i-st+1)
        return max_1
        