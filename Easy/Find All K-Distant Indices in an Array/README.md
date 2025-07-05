# 🔍 LeetCode 2200 – Find All K-Distant Indices in an Array

| Item            | Value                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------|
| **Solved on**   | 24‑JUNE‑2025                                                                                    |
| **Category**    | Easy                                                                                            |
| **Topic Tags**  | Array, Two Pointers                                                                             |
| **Problem Link**| [Find All K-Distant Indices in an Array](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/) |

---

## 📄 Problem Statement

Given an array `nums`, an integer `key`, and an integer `k`, return a list of all indices `i` such that there exists at least one index `j` where `nums[j] == key` and `abs(i - j) <= k`.

---

## 🧠 Approach

1. Traverse `nums` and store all indices where the value is equal to `key`.
2. For every index `i` in the array:
   - Check if `abs(i - j) <= k` for any `j` in the key indices.
   - If true, add `i` to the result.
3. Sort and return the result.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n * m)  
  where *n* is the length of `nums`, and *m* is the number of `key` occurrences  
- **Space Complexity:** O(n) for the result list

---

## ✅ Example

```python
Input:
nums = [1, 2, 3, 4, 2, 1, 2]
key = 2
k = 1

Key indices: [1, 4, 6]
Valid i: all 0 through 6 → abs(i - j) ≤ 1 for some j

Output: [0, 1, 2, 3, 4, 5, 6]
```
## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
