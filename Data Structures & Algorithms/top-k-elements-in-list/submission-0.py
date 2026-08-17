from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        topKeys = [key for key, count in counter.most_common(k)]

        return topKeys