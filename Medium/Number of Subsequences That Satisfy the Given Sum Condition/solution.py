# 1498. Number of Subsequences That Satisfy the Given Sum Condition
# Date: 2025-06-29
# Link: https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

"""
Approach:
- Sort the array
- For each number at index i, treat it as the minimum.
- Use binary search to find the farthest index j such that nums[i] + nums[j] <= target.
- The number of valid subsequences from i to j is 2^(j - i).
- Precompute powers of 2 for efficiency.

Time Complexity: O(n log n) [Sorting + Binary Search per index]
Space Complexity: O(n) [For power array]
"""

from bisect import bisect_right

class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        mod = 10**9 + 7
        n = len(nums)
        
        # Precompute powers of 2
        powers = [1] * n
        for i in range(1, n):
            powers[i] = (powers[i - 1] * 2) % mod

        result = 0

        for i in range(n):
            # Binary search for max j where nums[i] + nums[j] <= target
            remain = target - nums[i]
            j = bisect_right(nums, remain) - 1
            
            if j >= i:
                result = (result + powers[j - i]) % mod

        return result

# Example Test
if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubseq([3, 5, 6, 7], 9))  # Output: 4

