class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = dict()

        for i in range(len(nums)):
            l = nums[i]
            k = target - l
            if k in c.keys():
                return [c[k], i]
            c[l] = i