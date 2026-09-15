class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = {}
        
        
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            hashmap[nums[i]] += 1

        while k != 0:
            key1 = max(hashmap, key=hashmap.get)
            res.append(key1)
            del hashmap[key1]
            k -= 1
        
        return res
