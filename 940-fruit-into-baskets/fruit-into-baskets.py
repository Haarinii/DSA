class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=r=maxlen=0
        mapp={}
        while r<len(fruits):
            mapp[fruits[r]]=mapp.get(fruits[r],0)+1
            while len(mapp)>2:
                mapp[fruits[l]]-=1
                if mapp[fruits[l]]==0:
                    del mapp[fruits[l]]
                l+=1
            if len(mapp)<=2:
                maxlen=max(maxlen,r-l+1)
                r+=1
        return maxlen  
        