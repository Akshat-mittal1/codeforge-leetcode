# 🔍 LeetCode 2311 – Longest Binary Subsequence Less Than or Equal to K

| Item            | Value                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------------|
| **Solved on**   | 29‑JUNE‑2025                                                                                               |
| **Category**    | Medium                                                                                                     |
| **Topic Tags**  | Greedy, String, Bit Manipulation                                                                           |
| **Problem Link**| [Longest Binary Subsequence Less Than or Equal to K](https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k) |

---

## 📄 Problem Statement

Given a binary string `s` and a positive integer `k`, return the **length of the longest subsequence** of `s` such that the **binary value** of the subsequence is less than or equal to `k`.

---

## 🧠 Approach

- Traverse the string from **right to left** (LSB to MSB).
- Always include `'0'` since it does not increase the value but increases the length.
- For `'1'`, include only if its value `2^power` keeps the total value ≤ `k`.
- Maintain `val` for current binary value and `power` for current bit index.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---

## ✅ Example

```python
Input:
s = "1001010"
k = 5

Subsequence: "00010"
Binary value = 2 ≤ 5
Length = 5

Output: 5
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)

