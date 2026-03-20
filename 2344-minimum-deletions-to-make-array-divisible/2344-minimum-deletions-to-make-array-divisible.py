from math import gcd
from functools import reduce

class Solution:
    def minOperations(self, nums, numsDivide):
        # Step 1: Compute GCD of numsDivide
        g = reduce(gcd, numsDivide)
        
        # Step 2: Sort nums
        nums.sort()
        
        # Step 3: Find smallest nums[i] that divides g
        for i, x in enumerate(nums):
            if g % x == 0:
                return i  # deletions needed
        
        # Step 4: No valid element found
        return -1
