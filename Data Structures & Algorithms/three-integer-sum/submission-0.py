class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sols = []

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) -1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    if [nums[i], nums[j], nums[k]] not in sols:
                        sols.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1

        return sols