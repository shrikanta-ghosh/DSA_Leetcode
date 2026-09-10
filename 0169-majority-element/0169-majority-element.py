class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        
        value = max(hash_map, key=hash_map.get)
        return value
        