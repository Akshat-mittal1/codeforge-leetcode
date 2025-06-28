# Title: Maximum Subsequence
# Date: 27-JUNE-2025
# LeetCode: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
# Approach: 
#   - Create an auxiliary array with each element’s index and value.
#   - Sort the array by value (descending), pick top k.
#   - Then sort by index (ascending) to maintain original order in the subsequence.
#   - Extract values only.
# Time Complexity: O(n log n)
# Space Complexity: O(n)


class Solution(object):
    def maxSubsequence(self, nums, k):
        n = len(nums)
        vals = [[i, nums[i]] for i in range(n)]  # auxiliary array
        vals.sort(key=lambda x: -x[1])           # sort by value descending
        vals = sorted(vals[:k])                  # pick k and sort by index
        res = [val for idx, val in vals]         # extract values
        return res


# Test Case
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubsequence([2, 1, 3, 3], 2))  # Output: [3, 3]
