class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      for i in range(len(nums)):

        for n in range(i + 1, len(nums)):
            if nums[i] == nums[n] :
                return True
     
        return False       

