class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high=0
        curr=0
        for i in gain:
            curr+=i
            high=max(high, curr)
        return high