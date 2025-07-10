# 🔍 LeetCode 66 – Plus One

| Item | Value |
|------|-------|
| **Solved on** | 09‑JULY‑2025 |
| **Category** | Easy |
| **Topic Tags** | Array, Math |
| **Problem Link** | [Plus One](https://leetcode.com/problems/plus-one/) |

---

## 📄 Problem Statement

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is a digit of the number (from most significant to least).  
Increment the number by one and return the resulting array.

---

## 🧠 Approach

- Convert the list of digits to an integer by multiplying and adding each digit.
- Increment the integer by 1.
- Reconvert the new number back into an array of digits using math (without string conversion).

---

## ⏱️ Time & Space Complexity

- **Time Complexity**: O(n) — single pass to convert and rebuild digits
- **Space Complexity**: O(n) — for storing output list

---

## ✅ Example

```python
Input: digits = [1, 2, 3]
Output: [1, 2, 4]

Input: digits = [9, 9, 9]
Output: [1, 0, 0, 0]
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
