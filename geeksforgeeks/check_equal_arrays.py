# https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1

class Solution:
    def check(self, A, B, N):
        from collections import Counter
        return Counter(A) == Counter(B)
