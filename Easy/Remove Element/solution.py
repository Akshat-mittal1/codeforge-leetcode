# 🔍 Problem: Remove Element
# 📍 Link: https://leetcode.com/problems/remove-element/
# 📂 Category: Easy
# 📅 Date Solved: 12-JUNE-2025

"""
🧠 Approach:
- Count how many times the target value `val` appears.
- Remove all occurrences of `val` from the list using `remove()`.
- Append underscores to maintain original list length (for visualization only).
- Return the count of non-`val` elements.

⏱️ Time Complexity: O(n^2) due to repeated `remove()` calls
📦 Space Complexity: O(1)
"""

class Solution(object):
    def removeElement(self, nums, val):
        l = len(nums)
        c = l - nums.count(val)
        while val in nums:
            nums.remove(val)
        for _ in range(l - c):
            nums.append('_')  # Optional, for visualization
        return c

# ✅ Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    k = sol.removeElement(nums, val)
    print("New length:", k)           # Output: 2
    print("Modified nums:", nums)     # Output: [2, 2, '_', '_'].
