class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            c = dict()
            
            for i in nums:
                if c.get(i) == 1:
                    return True
                c[i] = 1
            return False