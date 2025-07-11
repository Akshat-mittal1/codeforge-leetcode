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
