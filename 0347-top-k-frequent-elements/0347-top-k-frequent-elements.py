class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i],0)+1
        sorted_keys = sorted(hash_map, key=hash_map.get, reverse=True)
        result = []
        for j in range(k):
            result.append(sorted_keys[j])
        return result