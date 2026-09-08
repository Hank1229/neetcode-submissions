class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in hash:
                return [hash[complement],i]
            
            hash[n] = i
        return[]
