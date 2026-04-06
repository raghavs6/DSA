class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       """
       we have an ordered array and a target number 
       and we need to find two index such that index1 < index2
       there will always be a solution

       my appraoch: 

       use a two pointer appraoch since its already sorted and need o(1) space
       then check if target is equal to sum if not increment l or r pointer

       """
       l, r = 0, len(numbers) - 1

       while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
       return []
       

       