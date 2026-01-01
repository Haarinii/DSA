class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s=0
        e=len(numbers)-1
        while(s<e):
            cur=numbers[s]+numbers[e]
            if cur==target:
                return [s+1,e+1]
            elif cur>target:
                e-=1
            else:
                s+=1
        

                
