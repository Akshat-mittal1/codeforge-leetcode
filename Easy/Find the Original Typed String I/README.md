# 🔍 LeetCode 3330 – Find the Original Typed String I

| Item            | Value                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------|
| **Solved on**   | 01‑JULY‑2025                                                                              |
| **Category**    | Easy                                                                                      |
| **Topic Tags**  | String, Greedy                                                                            |
| **Problem Link**| [Find the Original Typed String I](https://leetcode.com/problems/find-the-original-typed-string-i/) |

---

## 📄 Problem Statement

You are given a string. Count how many positions in the string have a character equal to the previous one.  
This represents possible positions where you could make a substitution or mark repetition, preserving the order.

---

## 🧠 Approach

- Start with a counter `a = 1` (the original string is always valid).
- Iterate from the second character to the end.
- If current character is same as previous, increment the counter.
- Return the final count.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n), where *n* is the length of the string  
- **Space Complexity:** O(1)

---

## ✅ Example

```python
Input: "aabbcc"

Steps:
- a == a → count = 2
- b == b → count = 3
- c == c → count = 4

Since we start from 1 (original string), total result = 4

Output: 4

```

## ---

👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
