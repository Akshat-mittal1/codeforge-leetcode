# 1498. Number of Subsequences That Satisfy the Given Sum Condition

**Date**: 29-JUNE-2025  
**Link**: [Leetcode Problem](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition)  
**Category**: Array, Two Pointers, Binary Search, Sorting

---

## 🧠 Problem Statement

You are given an array of integers `nums` and an integer `target`.  
Return the number of non-empty **subsequences** such that the **sum of the minimum and maximum** element in it is less than or equal to `target`.  
Return the answer modulo **10⁹ + 7**.

---

## 🔍 Approach

1. **Sort the array**.
2. For each index `i`, treat `nums[i]` as the minimum.
3. Use **binary search** to find the **maximum index j** such that:
   - `nums[i] + nums[j] <= target`
4. All elements from `i` to `j` can form subsequences — count is:
   - `2^(j - i)`
5. Use a precomputed powers-of-2 list to optimize performance.

---

## 🧮 Formula

If:
- `nums[i]` is the minimum
- `j` is the last index where `nums[i] + nums[j] <= target`

Then:
Valid subsequences = 2^(j - i)

yaml
Copy
Edit

---

## ⏱ Time & Space Complexity

| Metric           | Complexity |
|------------------|------------|
| Time Complexity  | O(n log n) |
| Space Complexity | O(n)       |

---

## 🔍 Example

**Input**:  
`nums = [3,5,6,7], target = 9`  
**Output**: `4`

**Valid Subsequences**:
- [3]
- [3,5]
- [3,6]
- [3,5,6]

---

## 👨‍💻 Solved By

**Akshat Mittal**
