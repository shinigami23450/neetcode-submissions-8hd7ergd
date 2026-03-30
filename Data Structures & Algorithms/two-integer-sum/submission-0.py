class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = dict()

        for i in range(len(nums)):
            k = target - nums[i]
            if k in c.keys():
                return [c[k], i]
            c[nums[i]] = i