class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        previous = {}
        for i in range(len(nums)):
            
            j = target - nums[i]
            if j in previous:
                
                return [previous[j], i]
            previous[j] = i    