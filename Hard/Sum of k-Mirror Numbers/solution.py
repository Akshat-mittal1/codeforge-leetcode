# 🔍 Problem: K-Mirror Numbers
# 📅 Date: 23-JUNE-2025
# 🔗 Link: https://leetcode.com/problems/k-mirror-numbers/
# ✅ Category: Math, Palindromes, Base Conversion
# 👨‍💻 Author: Akshat Mittal

class Solution:
    def createPalindrome(self, num: int, odd: bool) -> int:
        x = num
        if odd:
            x //= 10
        while x > 0:
            num = num * 10 + x % 10
            x //= 10
        return num

    def isPalindrome(self, num: int, base: int) -> bool:
        digits = []
        while num > 0:
            digits.append(num % base)
            num //= base
        return digits == digits[::-1]

    def kMirror(self, k: int, n: int) -> int:
        total = 0
        length = 1
        while n > 0:
            # Odd-length palindromes
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.createPalindrome(i, True)
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1
            # Even-length palindromes
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.createPalindrome(i, False)
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1
            length *= 10
        return total


# 🧪 Dry Run / Test Block
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    k = 2
    n = 5
    print(f"First {n} k-mirror numbers in base {k} sum to:", sol.kMirror(k, n))
    # Expected Output: 25

    # Example 2 (Uncomment for custom input)
    # k = int(input("Enter base k: "))
    # n = int(input("Enter number of k-mirror numbers: "))
    # print("Sum of first", n, "k-mirror numbers:", sol.kMirror(k, n))
