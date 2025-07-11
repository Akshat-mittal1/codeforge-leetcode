# 🔍 LeetCode 2040 – K-th Smallest Product of Two Sorted Arrays

| Item            | Value                                                                                      |
|-----------------|---------------------------------------------------------------------------------------------|
| **Solved on**   | 25‑JUNE‑2025                                                                               |
| **Category**    | Hard                                                                                       |
| **Topic Tags**  | Binary Search, Two Pointers, Sorting                                                       |
| **Problem Link**| [K-th Smallest Product of Two Sorted Arrays](https://leetcode.com/problems/k-th-smallest-product-of-two-sorted-arrays/) |

---

## 📄 Problem Statement

Given two sorted arrays `nums1` and `nums2`, and an integer `k`,  
return the `k-th` smallest product of `nums1[i] * nums2[j]`.

---

## 🧠 Approach

We perform **binary search on the answer range** (i.e., the product space).  
For a given `mid`, we count how many pairs `(i, j)` satisfy `nums1[i] * nums2[j] <= mid` using binary search (`bisect`).

- If `a > 0`: count how many `b` satisfy `b <= mid // a`
- If `a < 0`: count how many `b` satisfy `b >= ceil(mid / a)`
- If `a == 0`: include all if `mid >= 0`

We adjust the search space (`low`, `high`) until we find the smallest number such that at least `k` products are `<= mid`.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O((m + n) × log(2e10))  
- **Space Complexity:** O(1)

---

## ✅ Example

```python
Input:
nums1 = [-4, -2, 0, 3]
nums2 = [1, 2]
k = 6

Products:
- [-4, -2, 0, 3] × [1, 2]
→ [-4, -8, -2, -6, 0, 0, 3, 6]

Sorted Products: [-8, -6, -4, -2, 0, 0, 3, 6]
6th smallest = 0

Output: 0
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
