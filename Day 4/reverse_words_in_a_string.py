# https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        str_arr = s.split()
        str_arr = str_arr[::-1]
        return " ".join(str_arr)