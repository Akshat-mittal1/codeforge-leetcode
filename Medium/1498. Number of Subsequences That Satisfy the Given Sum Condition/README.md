# 🔍 LeetCode 1498 – Number of Subsequences That Satisfy the Given Sum Condition

| Item            | Value                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------------|
| **Solved on**   | 29‑JUNE‑2025                                                                                                              |
| **Category**    | Medium                                                                                                                   |
| **Topic Tags**  | Array, Two Pointers, Binary Search, Sorting                                                                             |
| **Problem Link**| [Number of Subsequences That Satisfy the Given Sum Condition](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition) |

---

## 📄 Problem Statement

You are given an array of integers `nums` and an integer `target`.

Return the number of non-empty **subsequences** such that the **sum of the minimum and maximum** element in the subsequence is less than or equal to `target`.  
Return the result modulo **10⁹ + 7**.

---

## 🧠 Approach

1. **Sort** the array.
2. Iterate each index `i` as the minimum element.
3. Use **binary search** to find the rightmost index `j` such that:
   - `nums[i] + nums[j] <= target`
4. All elements from `i` to `j` can form valid subsequences.
5. The number of such subsequences is `2^(j - i)`.

To avoid TLE:
- Precompute powers of 2 modulo `10⁹ + 7` for all indices.

---

## ⏱️ Time & Space Complexity

| Type              | Value       |
|-------------------|-------------|
| Time Complexity   | O(n log n)  |
| Space Complexity  | O(n)        |

---

## ✅ Example

```python
Input: nums = [3, 5, 6, 7], target = 9

Valid Subsequences:
- [3]
- [3,5]
- [3,6]
- [3,5,6]

Output: 4
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
