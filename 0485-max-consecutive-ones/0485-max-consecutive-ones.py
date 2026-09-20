class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        current_count = 0
        max_count = 0
        for i in nums:
            if i==1:
                current_count+=1
            elif i!=1:
                current_count = 0
            max_count = max(max_count, current_count)
        return max_count