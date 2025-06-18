# 🔍 Problem: Two Sum
# 📍 Link: https://leetcode.com/problems/two-sum/
# 📂 Category: Easy
# 📅 Date Solved: 20-DEC-2024

"""
🧠 Approach:
- Use a dictionary to store each number's index.
- For each number, check if target - num is already in dictionary.
- If found, return both indices.

⏱️ Time Complexity: O(n)
📦 Space Complexity: O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = {}  # Dictionary to store number and its index

        for i, item in enumerate(nums):
            find = target - item
            if find in n:
                return [n[find], i]
            n[item] = i  # Store the index of the current number

# ✅ Example usage
if __name__ == "__main__":
    sol = Solution()
    result = sol.twoSum([2, 7, 11, 15], 9)
    print("Output:", result)  # Output: [0, 1]
