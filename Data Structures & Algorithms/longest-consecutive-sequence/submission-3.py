class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        nums.sort()
        

        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i + 1] == nums[i] + 1:
                count += 1
        return count


