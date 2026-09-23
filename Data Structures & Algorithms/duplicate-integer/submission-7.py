class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      for i in range(len(nums)):

        for n in range(n+1,len(nums)):
            if nums[i] == nums[n+1] :
                return True
     
        return False       

