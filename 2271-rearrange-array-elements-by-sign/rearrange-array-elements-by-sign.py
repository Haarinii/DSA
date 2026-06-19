class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_position=0
        negative_position=1
        answer=[0]*len(nums)
        for i in nums:
            if i>0:
                answer[positive_position]=i
                positive_position+=2
            else:
                answer[negative_position]=i
                negative_position+=2
        return answer
        