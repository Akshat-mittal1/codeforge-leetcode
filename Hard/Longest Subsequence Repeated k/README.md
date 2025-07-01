# Longest Subsequence Repeated K Times
**Date**: 2025-07-01  
**Link**: [LeetCode Problem](https://leetcode.com/problems/longest-subsequence-repeated-k-times/)  
**Category**: Greedy, BFS, Subsequence

---

### Problem Statement:
Given a string `s` and an integer `k`, return the longest subsequence `sub` such that `sub` repeated `k` times is a subsequence of `s`. If multiple answers exist, return the lexicographically largest one.

---

### Approach:
- Count frequencies of characters and filter those with frequency ≥ k.
- Use BFS to generate subsequences in increasing length.
- For each candidate, check if repeating it `k` times is still a subsequence of `s`.
- Keep updating the result if a longer or lexicographically greater valid subsequence is found.

---

### Key Function:
```python
def isValid(sub):
    t = sub * k
    # Check if t is a subsequence of s
Time & Space Complexity:
Time: Exponential (due to branching on character combinations)

Space: O(n) for queue and result storage

Example:
python
Copy
Edit
Input: s = "letsleetcode", k = 2
Output: "let"
Explanation: "letlet" is a subsequence of the input string.
Author: Akshat Mittal
