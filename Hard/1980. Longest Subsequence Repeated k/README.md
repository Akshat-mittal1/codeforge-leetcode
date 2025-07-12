# 🔍 LeetCode 1980 – Longest Subsequence Repeated K Times

| Item            | Value                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------|
| **Solved on**   | 27‑JUNE‑2025                                                                                    |
| **Category**    | Hard                                                                                            |
| **Topic Tags**  | Greedy, BFS, Subsequence                                                                        |
| **Problem Link**| [Longest Subsequence Repeated K Times](https://leetcode.com/problems/longest-subsequence-repeated-k-times/) |

---

## 📄 Problem Statement

Given a string `s` and an integer `k`, return the **longest subsequence** `sub` such that `sub` repeated `k` times is a subsequence of `s`.  
If multiple answers exist, return the **lexicographically largest** one.

---

## 🧠 Approach

- Count frequency of each character in `s` and keep only those that appear at least `k` times.
- Use **BFS** to generate all possible subsequences using the valid character set.
- For each candidate `sub`:
  - Check whether `sub * k` is a subsequence of `s`.
  - If yes, update the result if it's longer or lexicographically larger than the previous.
- Always try larger lexicographic characters first (to favor larger subsequence).

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** Exponential (branching factor per character)
- **Space Complexity:** O(n) for queue and result storage

---

## ✅ Example

```python
Input:
s = "letsleetcode"
k = 2

Check: Is "let" × 2 = "letlet" a subsequence of s?

Yes → Valid

Output: "let"
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
