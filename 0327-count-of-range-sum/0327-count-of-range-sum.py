class Solution:
    def countRangeSum(self, nums, lower, upper):
        # Step 1: Build prefix sums
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        # Step 2: Modified merge sort
        def sort_and_count(left, right):
            if right - left <= 1:
                return 0

            mid = (left + right) // 2
            count = sort_and_count(left, mid) + sort_and_count(mid, right)

            j = k = mid
            temp = []
            r = mid

            # Count valid ranges
            for i in range(left, mid):
                while k < right and prefix[k] - prefix[i] < lower:
                    k += 1
                while j < right and prefix[j] - prefix[i] <= upper:
                    j += 1
                count += j - k

            # Merge step
            l = left
            r = mid
            while l < mid and r < right:
                if prefix[l] <= prefix[r]:
                    temp.append(prefix[l])
                    l += 1
                else:
                    temp.append(prefix[r])
                    r += 1
            temp.extend(prefix[l:mid])
            temp.extend(prefix[r:right])
            prefix[left:right] = temp

            return count

        return sort_and_count(0, len(prefix))
