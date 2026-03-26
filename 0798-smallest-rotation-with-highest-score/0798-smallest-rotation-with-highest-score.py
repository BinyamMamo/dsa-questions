class Solution:
    def bestRotation(self, nums):
        n = len(nums)
        change = [0] * (n + 1)

        for i, val in enumerate(nums):
            # When does this element start scoring?
            start = (i + 1) % n
            # When does it stop scoring?
            end = (i - val + n + 1) % n

            change[start] += 1
            change[end] -= 1

            if start > end:
                change[0] += 1

        best = -1
        score = 0
        max_score = -1

        for k in range(n):
            score += change[k]
            if score > max_score:
                max_score = score
                best = k

        return best
