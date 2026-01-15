class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                left = flowerbed[i-1] if i > 0 else 0
                right = flowerbed[i+1] if i < len(flowerbed)-1 else 0
                if left==0 and right==0:
                    flowerbed[i]=1
                    count+=1
        if count>=n:
            return True
        else:
            return False