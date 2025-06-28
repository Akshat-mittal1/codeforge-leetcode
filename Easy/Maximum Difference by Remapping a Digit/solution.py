# Title: Maximum Difference by Remapping a Digit
# Date: 2025-06-27
# LeetCode: https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/
# Approach:
#   - Convert input number to string to identify:
#     • For max: replace the first non-9 digit with 9
#     • For min: replace the first digit with 0
#   - Reconstruct max and min by replacing digit-wise
# Time Complexity: O(d) where d = number of digits
# Space Complexity: O(1)
# Dry Run:
#   num = 11891 → max = 99899, min = 11001 → result = 99899 - 11001 = 88898

class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        fmin = num[0]  # digit to replace with 0 for min
        fmax = '9'     # digit to replace with 9 for max

        # find first digit other than 9 to replace for max
        for i in num:
            if i != '9':
                fmax = i
                break

        le = len(num)
        num = int(num)
        max_val = 0
        min_val = 0

        while le > 0:
            r = num // (10 ** (le - 1))  # extract leftmost digit

            # build min by replacing fmin with 0
            if r == int(fmin):
                min_val = min_val * 10 + 0
            else:
                min_val = min_val * 10 + r

            # build max by replacing fmax with 9
            if r == int(fmax):
                max_val = max_val * 10 + 9
            else:
                max_val = max_val * 10 + r

            num -= r * (10 ** (le - 1))
            le -= 1

        return max_val - min_val


# Test Case
if __name__ == "__main__":
    sol = Solution()
    print(sol.minMaxDifference(11891))  # Output: 88898

