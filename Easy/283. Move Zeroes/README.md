# 🔍 LeetCode 283 – Move Zeroes

| Item | Value |
|------|-------|
| **Solved on** | 08‑JULY‑2025 |
| **Category** | Easy |
| **Topic Tags** | Array, Two Pointers |
| **Problem Link** | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) |

---

## 📄 Problem Statement

Given an integer array `nums`, move all `0`'s to the **end** of it while maintaining the **relative order** of the non-zero elements.

You **must do this in-place** without making a copy of the array.

---

## 🧠 Approach

- Use a **two-pointer technique**.
- Maintain a `change` pointer that tracks where the next non-zero element should go.
- Iterate through the list:
  - If the current element is not 0 and it's not already in the right place, swap it with `nums[change]`.
  - Increment `change` for each non-zero.
- This ensures all non-zero elements are pushed forward and zeroes are shifted to the end.

---

## ⏱️ Time & Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

---

## ✅ Example

```python
Input: nums = [0, 1, 0, 3, 12]
Step-by-step:
- Swap nums[1] and nums[0] → [1, 0, 0, 3, 12]
- Swap nums[3] and nums[1] → [1, 3, 0, 0, 12]
- Swap nums[4] and nums[2] → [1, 3, 12, 0, 0]

Output: [1, 3, 12, 0, 0]
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
