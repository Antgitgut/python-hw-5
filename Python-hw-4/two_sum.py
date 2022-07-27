from typing import List


def twoSum(nums: List[int], target: int):
    for i in nums:
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:

                print([i, j])
                input()
                return


twoSum([1, 6, 6, 1, 3, 3, 3], 9)
