# K-th Smallest Product of Two Sorted Arrays

**Date:** 2025-06-26  
**Link:** [LeetCode](https://leetcode.com/problems/k-th-smallest-product-of-two-sorted-arrays/)  
**Category:** Binary Search on Answer

---

### 🧠 Problem Statement:
Given two sorted arrays `nums1` and `nums2`, and an integer `k`, return the `k-th` smallest product of `nums1[i] * nums2[j]`.

---

### 💡 Approach:
We perform **binary search on the answer range** (product space).  
For a given mid, we count how many pairs have product ≤ mid using two-pointer-like logic (optimized with `bisect`).  
- For positive `a`: find how many `b` are ≤ `mid // a`
- For negative `a`: find how many `b` are ≥ ceil(`mid / a`)
- For zero: all products are 0 (included if `mid ≥ 0`)

---

### 📌 Formula:
For `a > 0`: count += bisect_right(nums2, mid // a)  
For `a < 0`: count += len(nums2) - bisect_left(nums2, ceil(mid / a))  
For `a == 0` and `mid >= 0`: all products are ≤ mid

---

### ⏱️ Time & Space:
- **Time:** O((m + n) * log(2e10))  
- **Space:** O(1)

---

### 🔁 Example:

```python
Input: nums1 = [-4, -2, 0, 3], nums2 = [1, 2], k = 6  
Output: 0

Explanation: Products = [-8, -4, 0, -2, 0, 0, 3, 6] → Sorted → Pick 6th smallest = 0
