class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m,c = nums[0], 0

        for n in nums:
            if c < 0:
                c = 0
            c += n
            m = max(c, m)
        return m
        

         


            