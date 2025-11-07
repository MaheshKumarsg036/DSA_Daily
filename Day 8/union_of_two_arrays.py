# https://practice.geeksforgeeks.org/problems/union-of-two-arrays/0

class Solution:    
    def findUnion(self, a, b):
        # code here
        a.sort()
        b.sort()
        i = 0
        j = 0
        ans = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                ans.append(a[i])
                i += 1
            elif a[i] > b[j]:
                ans.append(b[j])
                j += 1
            elif a[i] == b[j]:
                ans.append(a[i])
                i += 1
                j += 1
            
        while i < len(a):
            if a[i] != ans[-1]:
                ans.append(a[i])
            i += 1
        while j < len(b):
            if b[j] != ans[-1]:
                ans.append(b[j])
            j += 1
        return set(ans)