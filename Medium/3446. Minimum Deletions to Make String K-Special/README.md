# 🔍 LeetCode 3446 – Minimum Deletions to Make String K-Special

| Item            | Value                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------|
| **Solved on**   | 21‑JUNE‑2025                                                                                            |
| **Category**    | Medium                                                                                                  |
| **Topic Tags**  | Greedy, Frequency Analysis                                                                              |
| **Problem Link**| [Minimum Deletions to Make String K-Special](https://leetcode.com/problems/minimum-deletions-to-make-string-k-special) |

---

## 📄 Problem Statement

You are given a string `word` and an integer `k`.

A string is called **k-special** if for all characters `i` and `j`:



|freq(i) - freq(j)| <= k

Return the **minimum number of deletions** required to make the string k-special.

---

## 🧠 Approach (Greedy + Sorted Frequencies)

1. Count the frequency of each character in the string.
2. Sort all the frequencies.
3. For every possible frequency value as the **base minimum**:
   - Delete characters that appear less than this value.
   - Reduce characters that appear more than `base + k` down to `base + k`.
4. Track the **minimum deletions** required across all valid frequency bases.

---

## ⏱️ Time & Space Complexity

| Type              | Value      |
|-------------------|------------|
| Time Complexity   | O(n²)      |
| Space Complexity  | O(n)       |

---

## ✅ Example

```python
Input: word = "aabbcccc", k = 1

Frequencies: a:2, b:2, c:4  
Try base = 2 → reduce c:4 → 3 deletions  
Try base = 3 → delete a,b: total 4 deletions  
→ Minimum deletions = 1

Output: 1
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
