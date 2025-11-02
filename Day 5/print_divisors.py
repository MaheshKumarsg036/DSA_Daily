#https://www.naukri.com/code360/problems/print-all-divisors-of-a-number_1164188?
from typing import List

def printDivisors(n: int) -> List[int]:
    # Write your code here
    i = 1
    ans = []
    while i <= n:
        if n % i == 0:
            ans.append(i)
        i += 1
    return ans
    