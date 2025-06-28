# Maximum Subsequence

**Date**: 2025-06-27  
**Link**: [LeetCode - Maximum Subsequence](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/)  
**Category**: Arrays, Greedy, Sorting

---

## 🧩 Problem Statement

You are given an integer array `nums` and an integer `k`.  
Return the subsequence of `nums` of length `k` that has the largest sum.

The answer must maintain the relative order of the elements in `nums`.

---

## 🚀 Approach

1. Store `(index, value)` pairs for each element in `nums`.
2. Sort the list in descending order of value.
3. Pick the top `k` items.
4. Sort them back based on original indices (to maintain order).
5. Extract only the values from the result.

---

## 📐 Formula / Key Step

- Sort by value ↓  
- Take top `k`  
- Sort by original index ↑

---

## ⏱️ Time & Space Complexity

- **Time**: `O(n log n)`  
- **Space**: `O(n)`

---

## 💡 Example

```python
Input: nums = [2, 1, 3, 3], k = 2  
Output: [3, 3]

