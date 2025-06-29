# 2311. Longest Binary Subsequence Less Than or Equal to K
# Date: 26-JUNE-2025
# Link: https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

"""
Approach:
- Iterate from right to left (least significant bit first).
- Always count '0' because it doesn't change binary value but increases subsequence length.
- For each '1', add its binary value only if total value so far stays <= k.
- Track the power of 2 and update value accordingly.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        power = 0
        count = 0
        val = 0
        n = len(s)

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                count += 1
            else:
                if power < 64:
                    val += (1 << power)
                    if val <= k:
                        count += 1
            power += 1

        return count

# Example Test
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubsequence("1001010", 5))  # Output: 5

