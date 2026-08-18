class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = max(piles)
        minK = 1

        while minK < maxK:
            midK = (minK + maxK) // 2
            hours = h

            for pile in piles:
                hours -= (math.ceil(pile/midK))
                if hours < 0:
                    break
            if hours < 0:
                minK = midK + 1
            else:
                maxK = midK
        return minK
