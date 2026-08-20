class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = arr[-1]
        arr[-1] = -1
        for i in reversed(range(len(arr)-1)):
            temp = arr[i]
            arr[i] = greatest
            greatest = max(greatest, temp)
        return arr