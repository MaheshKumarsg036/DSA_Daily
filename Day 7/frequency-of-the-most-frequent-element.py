# https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l =0
        r = 0
        n = len(nums)
        ans = 0
        total = 0

        while r < n:
            total += nums[r]

            while nums[r]*(r-l+1) > total+k:
                total -= nums[l]
                l += 1
            if (r-l+1) > ans:
                ans = r-l+1
            r += 1
        return ans
