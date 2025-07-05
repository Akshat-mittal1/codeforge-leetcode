# 🔍 LeetCode 594 – Longest Harmonious Subsequence

| Item            | Value                                                                                  |
|-----------------|----------------------------------------------------------------------------------------|
| **Solved on**   | 30‑JUNE‑2025                                                                           |
| **Category**    | Easy                                                                                   |
| **Topic Tags**  | Array, HashMap, Two Pointers                                                           |
| **Problem Link**| [Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence/) |

---

## 📄 Problem Statement

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.  
Given an integer array `nums`, return the length of the longest harmonious subsequence among all its possible subsequences.

---

## 🧠 Approach

- Sort the array
- Use two pointers (`j` and `i`) to find the longest window where `nums[i] - nums[j] == 1`
- Update max length accordingly

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n log n) — due to sorting  
- **Space Complexity:** O(1) — no extra memory used

---

## ✅ Example

```python
Input: nums = [1, 3, 2, 2, 5, 2, 3, 7]

Steps:
- Sorted: [1, 2, 2, 2, 3, 3, 5, 7]
- Longest subsequence with max - min == 1 → [2, 2, 2, 3, 3]

Output: 5
```

##  👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
