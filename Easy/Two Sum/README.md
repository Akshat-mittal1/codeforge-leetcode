# 🔍 LeetCode 1 – Two Sum

| Item            | Value                                            |
|-----------------|--------------------------------------------------|
| **Solved on**   | 20‑DECEMBER‑2024                                 |
| **Category**    | Easy                                             |
| **Topic Tags**  | Hash Map, Array                                  |
| **Problem Link**| [Two Sum](https://leetcode.com/problems/two-sum/) |

---

## 📄 Problem Statement

Given an array of integers `nums` and an integer `target`,  
return indices of the **two numbers** such that they **add up to `target`**.

You may assume that each input has **exactly one solution**,  
and you may not use the same element twice.

Return the answer in **any order**.

---

## 🧠 Approach (Hash Map Lookup)

- Loop through the array using `enumerate`.
- For each element:
  - Calculate `find = target - current`.
  - If `find` already exists in a dictionary `n`, return the current index and the index of `find`.
  - Else, store the current number with its index in the dictionary.
- Dictionary allows **O(1)** lookups.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n), where *n* is the length of the array  
- **Space Complexity:** O(n) for the hash map

---

## ✅ Example

```python
Input: nums = [2, 7, 11, 15], target = 9

Steps:
- i = 0 → num = 2 → find = 7 → not in dict
- i = 1 → num = 7 → find = 2 → found in dict at index 0

Output: [0, 1]
```
👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
