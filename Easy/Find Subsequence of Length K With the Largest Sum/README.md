# 🔍 LeetCode 2099 – Find Subsequence of Length K With the Largest Sum

| Item            | Value                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| **Solved on**   | 27‑JUNE‑2025                                                                                              |
| **Category**    | Medium                                                                                                    |
| **Topic Tags**  | Arrays, Greedy, Sorting                                                                                   |
| **Problem Link**| [Find Subsequence of Length K With the Largest Sum](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/) |

---

## 📄 Problem Statement

You are given an integer array `nums` and an integer `k`.  
Return the subsequence of `nums` of length `k` that has the largest sum.

The answer must maintain the relative order of the elements in `nums`.

---

## 🧠 Approach

1. Store `(index, value)` pairs for each element in `nums`.
2. Sort the list in descending order of value.
3. Pick the top `k` items.
4. Sort them back based on original indices (to maintain order).
5. Extract only the values from the result.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n log n)  
- **Space Complexity:** O(n)

---

## ✅ Example

```python
Input: nums = [2, 1, 3, 3], k = 2

Steps:
- Pair with index: [(0,2), (1,1), (2,3), (3,3)]
- Sort by value ↓ → [(2,3), (3,3), (0,2), (1,1)]
- Take top 2 → [(2,3), (3,3)]
- Sort by index ↑ → [(2,3), (3,3)]
- Extract values → [3, 3]

Output: [3, 3]
```

##  👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
