from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # Define recursive helper function
        def helper(i, prev, beautiful_sets):
            if i == len(nums):
                # Base case: reached end of array, add to beautiful sets if it meets requirements
                if len(prev) > 0:
                    beautiful_sets.add(tuple(sorted(prev)))
            else:
                # Recursive case: try adding or not adding current number to previous set
                if not prev or abs(nums[i] - prev[-1]) != k:
                    # If no previous number or difference with previous number is not k,
                    # try adding current number to previous set
                    helper(i + 1, prev + [nums[i]], beautiful_sets)
                # Try not adding current number to previous set
                helper(i + 1, prev, beautiful_sets)

        # Call recursive helper function to generate all beautiful subsets
        beautiful_sets = set()
        helper(0, [], beautiful_sets)

        # Return number of beautiful subsets
        return len(beautiful_sets)


s = Solution()
print(s.beautifulSubsets(nums=[2, 4, 6, 7, 8], k=2))

# [2,6,7,8]
# 2 6
# 2 7
# 2 8
# 2 6 7
# 2 6 8
# 2 7 8
# 2 6 7 8

# [2,6,7,8,9]
# 2 6
# 2 7
# 2 8
# 2 9
# 2 6 7
# 2 6 8
# 2 6 9
# 2 7 8
# 2 7 9
# 2 8 9
# 2 6 7 8
# 2 6 7 9
# 2 6 8 9
# 2 7 8 9
# 2 6 7 8 9
