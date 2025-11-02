# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1
        x = -1*x if x < 0 else x
        while x > 0:
            rev = rev *10 + x % 10
            x = x // 10
            if rev > 2**31 - 1:
                return 0
        return rev * sign
        