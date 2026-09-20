class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        nums_sq = []
        for i in range(len(nums)):
            sq = nums[i]*nums[i]
            nums_sq.append(sq)
        nums_sq.sort()
        return nums_sq