from typing import List

class Solution:
    def kidsWithCandies(self, candy_counts: List[int], extra_candies: int) -> List[bool]:
        highest_candy_count = max(candy_counts)
        results = []

        for current_count in candy_counts:
            can_be_greatest = current_count + extra_candies >= highest_candy_count
            results.append(can_be_greatest)

        return results
