#https://www.naukri.com/code360/problems/check-if-the-string-is-a-palindrome_1062633
from os import *
from sys import *
from collections import *
from math import *

def checkPalindrome(s):
    # Write your code here
	# Return a boolean
	l,r = 0,len(s)-1
    while l < r:
        if s[r] != s[l]:
            return "No"
        l += 1
        r -= 1
    return "Yes"