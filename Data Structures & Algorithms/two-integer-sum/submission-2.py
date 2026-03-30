class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = dict()

        for i, v in enumerate(nums):
            k = target - v
            if k in c:
                return [c[k], i]
            c[v] = i