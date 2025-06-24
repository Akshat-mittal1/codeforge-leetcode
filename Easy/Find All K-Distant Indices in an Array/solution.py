# 🔍 Problem: Find All K-Distant Indices in an Array
# 📅 Date: 2025-06-24
# 🔗 Link: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
# 🧠 Approach:
#   1. First, find all indices where nums[i] == key.
#   2. Then, for each index `i` in nums, check if the absolute distance
#      to any of the key indices is ≤ k.
#   3. If yes, include that index `i` in the result.
# 🕒 Time Complexity: O(n * m) where n = len(nums), m = count of `key` in nums
# 🧠 Space Complexity: O(n) for storing result indices
# ✅ Example:
#   Input: nums = [1,2,3,4,2,1,2], key = 2, k = 1
#   Output: [0, 1, 2, 3, 4, 5, 6]

class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        index = [i for i, val in enumerate(nums) if val == key]
        for i in range(len(nums)):
            for j in index:
                if abs(i - j) <= k:
                    res.append(i)
                    break
        res.sort()
        return res


# 🔁 Test Case
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 2, 1, 2]
    key = 2
    k = 1
    print(sol.findKDistantIndices(nums, key, k))  # Output: [0, 1, 2, 3, 4, 5, 6]
