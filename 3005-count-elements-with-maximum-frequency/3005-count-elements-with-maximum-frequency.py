class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i],0)+1
        max_val = max(hash_map.values())
        count=0
        for i in nums:
            if hash_map[i]==max_val:
                count = count+1
        return count
        