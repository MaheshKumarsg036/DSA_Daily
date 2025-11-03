# https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops3621/1

class Solution:
	def printTillN(self, N):
		# code here
		if N == 1:
			print(1, end=" ")
			return
		self.printTillN(N-1)
		print(N, end=" ")