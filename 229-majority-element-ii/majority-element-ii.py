class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1=count2=0
        ele1=ele2=float('-inf')
        for i in range (len(nums)):
            if count1==0 and ele2!=nums[i]:
                count1+=1
                ele1=nums[i]
            elif count2==0 and ele1!=nums[i]:
                count2+=1
                ele2=nums[i]
            elif nums[i]==ele1:
                count1+=1
            elif nums[i]==ele2:
                count2+=1
            else:
                count1-=1
                count2-=1
        lst=[]
        cnt1=cnt2=0
        for i in range(len(nums)):
            if nums[i]==ele1:
                cnt1+=1
            if nums[i]==ele2:
                cnt2+=1
        mm=(len(nums)//3)+1
        if cnt1>=mm:
            lst.append(ele1)
        if cnt2>=mm:
            lst.append(ele2)
        lst.sort()
        return lst
        