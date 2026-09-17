class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1

        for n in nums:
            tmp = curMax * n
            tmp2 = n * curMin
            curMax = max(tmp, tmp2, n)
            curMin = min(tmp, tmp2, n)
            res = max(res, curMax)
        return res
                
                    