# 🔍 LeetCode 28 – Find the Index of the First Occurrence in a String

| Item | Value |
|------|-------|
| **Solved on** | 08‑JULY‑2025 |
| **Category** | Easy |
| **Topic Tags** | String, Substring |
| **Problem Link** | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) |

---

## 📄 Problem Statement

Given two strings `haystack` and `needle`, return the index of the **first occurrence** of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

---

## 🧠 Approach

- Use Python’s built-in string method `str.index()` to search for the substring.
- If `needle` is in `haystack`, return the index.
- Otherwise, return `-1`.

This method is optimal and takes advantage of the efficient built-in search in Python.

---

## ⏱️ Time & Space Complexity

- **Time Complexity**: O(n * m) worst case, where `n = len(haystack)` and `m = len(needle)`
- **Space Complexity**: O(1)

---

## ✅ Example

```python
Input:
haystack = "hello", needle = "ll"
Output: 2

Input:
haystack = "leetcode", needle = "leeto"
Output: -1
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
