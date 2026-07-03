class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        ds=[]
        freq=[False]*len(nums)
        def f():
            if len(ds)==len(nums):
                ans.append(ds[:])
                return
            for i in range(len(nums)):
                if not freq[i]:
                    freq[i]=True
                    ds.append(nums[i])
                    f()
                    ds.pop()
                    freq[i]=False
        f()
        return ans  


       









    def f():
        ans=[]
        ds=[]
        freq=[]*False
