# Problem Title: Count Possible Strings Without Changing Order
# Date: 2025-07-01
# Problem Link: (Your link here, or custom problem)
# Approach: Count consecutive characters that are the same, each such repetition adds a possibility.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Test Case Included

class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        a = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                a += 1
        return a

# Example Test
sol = Solution()
print(sol.possibleStringCount("aabbcc"))  # Output: 3

