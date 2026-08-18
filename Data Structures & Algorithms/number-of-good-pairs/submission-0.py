from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)

        sum = 0
        for i in count.values():
            if i != 1:
                sum += int((i*(i-1))/2)
        return sum