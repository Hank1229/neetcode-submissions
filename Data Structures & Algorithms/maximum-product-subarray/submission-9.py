class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      res = max(nums)
      curMax, curMin = 1, 1

      for n in nums:
        
        tmpMax = n * curMax
        tmpMin = n * curMin

        curMax = max(tmpMax, tmpMin, n)
        curMin = min(tmpMax, tmpMin, n)
        res = max(curMax, res)

      return res
