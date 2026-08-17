class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1

        stored = 0

        while start < end:
            stored = max(stored, min(heights[start], heights[end])*(end-start))
            if heights[start] < heights[end]:
                start += 1
            else:
                end -=1
        
        return stored