# 🔍 LeetCode 7 – Reverse Integer

| Item            | Value                                                                                 |
|-----------------|----------------------------------------------------------------------------------------|
| **Solved on**   | 24‑JUNE‑2025                                                                           |
| **Category**    | Easy                                                                                   |
| **Topic Tags**  | Math, Integer Manipulation                                                             |
| **Problem Link**| [Reverse Integer](https://leetcode.com/problems/reverse-integer/)                      |

---

## 📄 Problem Statement

Given a signed 32-bit integer `x`, return `x` with its digits reversed.  
If reversing `x` causes the value to go **outside the signed 32-bit range** `[-2³¹, 2³¹ − 1]`, return `0`.

---

## 🧠 Approach

- Take the absolute value of `x`.
- Reverse it digit by digit:
  - Multiply the current reversed value by 10 and add the last digit (`x % 10`).
  - Then reduce the original number (`x = x // 10`).
- After reversal, **check for 32-bit overflow**.
- If `x` was negative, return `-reversed`; otherwise, return `reversed`.

---

## ⏱️ Time & Space Complexity

| Type             | Complexity  |
|------------------|-------------|
| Time Complexity  | O(log₁₀N)   |
| Space Complexity | O(1)        |

---

## ✅ Example

```
Input: x = -123
Steps:
- abs(-123) = 123
- Reverse = 321
- Since original was negative → Result = -321

Output: -321
python
Copy
Edit
Input: x = 120
Steps:
- abs(120) = 120
- Reverse = 21 (leading zero is dropped)
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)


Output: 21
