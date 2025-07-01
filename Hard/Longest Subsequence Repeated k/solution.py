# Problem Title: Longest Subsequence Repeated K Times
# Date: 27-JUNE-2025
# Problem Link: https://leetcode.com/problems/longest-subsequence-repeated-k-times/
# Approach: BFS + Greedy + Subsequence Validation
# Time Complexity: Exponential (due to BFS, worst case O(26^len))
# Space Complexity: O(n) for queue and result storage
# Test Case Included

from collections import Counter

class Solution(object):
    def longestSubsequenceRepeatedK(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def isValid(sub):
            t = sub * k
            n = len(t)
            i = 0
            for ch in s:
                if i < n and ch == t[i]:
                    i += 1
            return i == n

        counter = Counter(s)
        candidate = [ch for ch, freq in counter.items() if freq >= k]

        res = ''
        queue = ['']

        while queue:
            sub = queue.pop(0)
            for neigh in sorted(candidate):  # sort for lexicographical order
                new_sub = sub + neigh
                if not isValid(new_sub):
                    continue
                if len(new_sub) > len(res) or (len(new_sub) == len(res) and new_sub > res):
                    res = new_sub
                queue.append(new_sub)

        return res

# Example Test
sol = Solution()
print(sol.longestSubsequenceRepeatedK("letsleetcode", 2))  # Output: "let"

