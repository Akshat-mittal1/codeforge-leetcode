class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = 0
        for j in digits:
            i = i * 10 + j
        i += 1
        l = len(str(i))
        digits = []
        for j in range(l):
            x = i // (10 ** (l - 1 - j))
            digits.append(x)
            i -= x * (10 ** (l - 1 - j))
        return digits


# ✅ Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))   # Output: [1, 2, 4]
    print(sol.plusOne([9, 9, 9]))   # Output: [1, 0, 0, 0]
