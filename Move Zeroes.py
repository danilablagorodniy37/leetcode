class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        move = 0
        for x in range(len(nums)):
            if nums[x] != 0:
                nums[move], nums[x] = nums[x], nums[move]
                move += 1