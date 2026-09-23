class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        previous = {}
        for i in range(len(nums)):
            previous = nums[i]
            j = target - nums[i]
            if j == previous:
                result = nums[i,j]
                return result