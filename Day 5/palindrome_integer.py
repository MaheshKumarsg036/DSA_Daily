# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        n = x
        while n > 0:
            rev = rev*10 + n % 10
            n = n // 10
        return rev == x
        