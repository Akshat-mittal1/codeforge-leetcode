# 🔍 LeetCode 2016 – Maximum Difference Between Increasing Elements

| Item            | Value                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------|
| **Solved on**   | 16‑JUNE‑2025                                                                                    |
| **Category**    | Easy                                                                                            |
| **Topic Tags**  | Array, Greedy                                                                                   |
| **Problem Link**| [Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements/) |

---

## 📄 Problem Statement

You are given a 0-indexed integer array `nums` of size `n`. The **maximum difference** between two elements `nums[i]` and `nums[j]` is defined as:

> `nums[i] - nums[j]` where `i > j` and `nums[i] > nums[j]`.

Return the maximum such difference. If no such pair exists, return -1.

---

## 🧠 Approach

- Iterate through the array while tracking the minimum element encountered so far.
- For each element, calculate the difference with the current minimum.
- Update the maximum difference only if `nums[i] > premin`.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---

## ✅ Example

```python
Input: nums = [7, 1, 5, 4]

Steps:
- premin = 7 → update to 1
- max_diff = max(0, 5 - 1) = 4

Output: 4
```

## ---

👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
