class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        gandu = {}
        for i , val in enumerate(nums):
            complement = target - val
            if complement in gandu:
                return[gandu[complement] ,i]  
            gandu[val] = i