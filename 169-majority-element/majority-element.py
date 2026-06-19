class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element=None
        count=0
        for i in nums:
            if count==0:
                count+=1
                element= i
            elif i==element:
                count+=1
            else:
                count-=1
        check=0
        for i in nums:
            if i== element:
                check+=1
        if check> len(nums)//2:
            return element
        return -1