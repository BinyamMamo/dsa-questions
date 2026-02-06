# https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1

class Solution:
    def doUnion(self, a, n, b, m):
        return len(set(a) | set(b))
