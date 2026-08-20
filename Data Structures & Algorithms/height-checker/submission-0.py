class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        nums = 0

        heightsCopy = sorted(heights)

        for i in range(len(heights)):
            if heights[i] != heightsCopy[i]:
                nums += 1
        return nums