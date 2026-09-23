class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        for i in range(len(nums)):
            previous = nums[i]
            j = target - nums[i]
            if j == previous:
                return nums[i] & nums[j]