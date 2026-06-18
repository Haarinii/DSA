class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        count = 0
        summ = 0
        for num in nums:
            summ += num
            rem = summ - k
            if rem in hashmap:
                count += hashmap[rem]
            hashmap[summ] = hashmap.get(summ, 0) + 1
        return count
        