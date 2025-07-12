# 🔍 LeetCode – K-Mirror Numbers

| Item            | Value                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------|
| **Solved on**   | 23‑JUNE‑2025                                                                                       |
| **Category**    | Hard                                                                                               |
| **Topic Tags**  | Math, Palindrome, Base Conversion, Efficient Generation                                            |
| **Problem Link**| [K-Mirror Numbers](https://leetcode.com/problems/k-mirror-numbers/)                               |

---

## 📄 Problem Statement

A **k-mirror number** is a positive integer that is:
- A palindrome in base-10
- A palindrome in base-`k`

Given an integer `k` and `n`, return the **sum of the first `n` k-mirror numbers**.

---

## 🧠 Approach

- Generate decimal palindromes by reflecting half the number (odd and even lengths).
- Convert each number to base-`k` and check if it’s a palindrome.
- If both conditions are satisfied, include it in the running sum.
- Stop when you’ve found `n` valid numbers.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** Efficient due to palindrome generation
- **Space Complexity:** O(logN) for base conversion and digit storage

---

## ✅ Example

```python
Input:
k = 2
n = 5

Palindromes:
1 → binary: 1    ✅
3 → binary: 11   ✅
5 → binary: 101  ✅
7 → binary: 111  ✅
9 → binary: 1001 ✅

Output: 1 + 3 + 5 + 7 + 9 = 25
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
