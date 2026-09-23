class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      for i in range(len(nums)):

        for n in range(len(nums)):
            if nums[i] == nums[n+1] :
                return True
     
        return False       

