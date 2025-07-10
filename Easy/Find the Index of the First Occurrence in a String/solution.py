class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

# ✅ Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("hello", "ll"))  # Output: 2
    print(sol.strStr("aaaaa", "bba"))  # Output: -1


