# 🔍 LeetCode 3333 – Find the Original Typed String II

| Item              | Value                                                                |
|-------------------|----------------------------------------------------------------------|
| **Solved on**     | 02‑JULY‑2025                                                         |
| **Category**      | Medium                                                               |
| **Topic Tags**    | Dynamic Programming, Combinatorics, String Manipulation              |
| **Problem Link**  | [Find the Original Typed String II](https://leetcode.com/problems/find-the-original-typed-string-ii/) |

---

## 📄 Problem Statement

You are given a string `word`, which may contain groups of **consecutive identical characters** — simulating keys held down during typing.

You are also given an integer `k`.

Return the number of **different original strings of length `k`** that could have been typed such that no group contributes more characters than it has in `word`.

---

## 🧠 Approach

1. Perform **run-length encoding** on the input string to create a list of group sizes.
2. Let `groups = [g₁, g₂, ..., gₙ]` represent how many of each character we can use.
3. Use **dynamic programming** where `dp[i][j]` = number of ways to pick `j` characters from the first `i` groups.
4. Transition:
   - For each group `i` and each `t` from `0` to `min(j, groups[i-1])`, add `dp[i-1][j - t]`.
5. Use a **1D rolling array** for space optimization.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n × k), where `n = number of groups`
- **Space Complexity:** O(k)

---

## ✅ Example (with explanation)

```python
Input:
word = "aabbcc"
k = 3

Groups = [2, 2, 2]
We want to form strings of length 3 by selecting ≤2 from each group

Valid combinations:
- 'abc', 'aac', 'bbc', 'abb', etc.

Total Valid Strings = 8
Output: 8
```

##  👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
