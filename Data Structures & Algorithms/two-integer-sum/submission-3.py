class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        previous = {}
        for i in range(len(nums)):
            previous = nums[i]
            j = target - nums[i]
            if j == previous:
                result = result.append(nums[i]) 
                result = result.append(nums[j]) 
                return result