class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        a = x[::-1]
        return a == x

# ✅ Example usage
if __name__ == "__main__":
    sol = Solution()
    print("121 ➝", sol.isPalindrome(121))    # True
    print("-121 ➝", sol.isPalindrome(-121))  # False
    print("10 ➝", sol.isPalindrome(10))      # False
