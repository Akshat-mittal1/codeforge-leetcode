# 🔍 LeetCode 4 – Median of Two Sorted Arrays

| Item            | Value                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------|
| **Solved on**   | 24‑JUNE‑2025                                                                                    |
| **Category**    | Hard                                                                                            |
| **Topic Tags**  | Array, Binary Search (Optimized), Sorting                                                      |
| **Problem Link**| [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)      |

---

## 📄 Problem Statement

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The optimal requirement is **O(log (m+n))**, but this solution uses a simple **merge + sort** method.

---

## 🧠 Approach

- Concatenate both arrays: `new = nums1 + nums2`
- Sort the combined array.
- If total length is odd → return middle element.
- If even → return the average of the two middle elements.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O((m + n) log(m + n))  
- **Space Complexity:** O(m + n)

---

## ✅ Example

```python
Input:
nums1 = [1, 3]
nums2 = [2]

Steps:
- Combine: [1, 3] + [2] → [1, 3, 2]
- Sorted: [1, 2, 3]
- Median: 2.0 (middle element)

Output: 2.0
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
