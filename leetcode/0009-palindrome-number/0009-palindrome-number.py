class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)

        l = 0
        r = -1
        while abs(r - l) < len(x):
            if x[l] != x[r]:
                return False
            r += -1
            l += 1
        return True