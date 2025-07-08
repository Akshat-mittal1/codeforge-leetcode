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
