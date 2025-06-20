# 🔍 LeetCode 9 – Palindrome Number

| Item | Value |
|------|-------|
| **Solved on** | 20‑12‑2024 |
| **Category** | Easy |
| **Topic Tags** | Math, String |
| **Problem Link** | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) |

---

## 📄 Problem Statement

Given an integer `x`, return `True` if `x` is a **palindrome**, and `False` otherwise.

> A palindrome is a number that reads the same forward and backward.  
Examples: `121`, `1331`, `0`, `11` are palindromes.  
But `-121`, `10`, `123` are not.

---

## 🧠 Approach

- Convert the number to a string: `str(x)`
- Reverse the string: `x[::-1]`
- Compare the reversed string with the original

---

## ✅ Example

```python
Input: 121
Reversed: "121"
Match: Yes
Output: True
