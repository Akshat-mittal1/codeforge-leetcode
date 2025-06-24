# 🔍 Problem: Reverse Integer
# 📅 Date: 24-JUNE-2025
# 🔗 Link: https://leetcode.com/problems/reverse-integer/
# ✅ Approach: Digit extraction and reversal
# ⏱️ Time Complexity: O(log₁₀N)
# 📦 Space Complexity: O(1)
# 🧪 Test Case:
# Input: x = -123
# Reversed = -321
# Output: -321

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 0
        temp = abs(x)
        while temp > 0:
            s = s * 10 + (temp % 10)
            temp = temp // 10

        if s > (2**31 - 1) or s < (-2**31):
            return 0
        elif x < 0:
            return -s
        else:
            return s

# 🔁 Dry Run
if __name__ == "__main__":
    sol = Solution()
    print("Reverse of -123:", sol.reverse(-123))  # Output: -321
    print("Reverse of 120:", sol.reverse(120))    # Output: 21
