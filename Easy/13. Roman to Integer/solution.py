class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        l = len(s) - 1
        for j, i in enumerate(s):
            if i == 'M':
                c += 1000
            elif i == 'D':
                c += 500
            elif i == 'C':
                if j + 1 <= l and s[j + 1] in ('D', 'M'):
                    c -= 100
                    continue
                c += 100
            elif i == 'L':
                c += 50
            elif i == 'X':
                if j + 1 <= l and s[j + 1] in ('L', 'C'):
                    c -= 10
                    continue
                c += 10
            elif i == 'V':
                c += 5
            else:  # 'I'
                if j + 1 <= l and s[j + 1] in ('V', 'X'):
                    c -= 1
                    continue
                c += 1
        return c

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print("III ➝", sol.romanToInt("III"))       # 3
    print("LVIII ➝", sol.romanToInt("LVIII"))   # 58
    print("MCMXCIV ➝", sol.romanToInt("MCMXCIV"))  # 1994
