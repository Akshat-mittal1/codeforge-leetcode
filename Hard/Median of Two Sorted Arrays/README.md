# 🧮 Median of Two Sorted Arrays

- 📅 Date: 24-JUNE-2025  
- 🔗 [Leetcode Problem Link](https://leetcode.com/problems/median-of-two-sorted-arrays/)  
- 🗂️ Category: Array, Binary Search (optimized), Sorting

---

### 📘 Problem Statement:
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The optimal requirement is **O(log (m+n))**, but this solution uses a simple **merge + sort** method.

---

### 💡 Approach:

- Concatenate both arrays: `new = nums1 + nums2`
- Sort the array
- If length is even: return average of middle two
- If length is odd: return the middle element

---

### 🧮 Formula:
- `l = len(new)`
- If `l` is odd → `median = new[l // 2]`
- If `l` is even → `median = (new[l//2] + new[(l//2)-1]) / 2.0`

---

### ⏱️ Time & Space Complexity:

| Type | Complexity |
|------|------------|
| 🕒 Time | O((m+n) log(m+n)) |
| 💾 Space | O(m+n) |

---

### 🧪 Example:

```python
Input:
    nums1 = [1, 3]
    nums2 = [2]
Steps:
    new = [1, 3] + [2] → [1, 3, 2]
    Sorted = [1, 2, 3]
    Median = 2.0 (middle element)

Output: 2.0
