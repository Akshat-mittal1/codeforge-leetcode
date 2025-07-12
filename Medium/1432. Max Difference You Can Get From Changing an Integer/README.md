# 🔍 LeetCode 1432 – Max Difference You Can Get From Changing an Integer

| Item            | Value                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| **Solved on**   | 15‑JUNE‑2025                                                                                               |
| **Category**    | Medium                                                                                                     |
| **Topic Tags**  | Greedy, String Manipulation                                                                                |
| **Problem Link**| [Max Difference You Can Get From Changing an Integer](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/) |

---

## 📄 Problem Statement

You are given an integer `num`. You can choose two digits (not necessarily distinct) and replace **all occurrences** of the first digit in `num` with the second digit.

- You must do this for **two separate replacements**:
  - One to get the **maximum** number possible
  - One to get the **minimum** number possible

Return the **difference between max and min** you can achieve after both operations.

---

## 🧠 Approach (Greedy Replacement)

- Convert the number to a string.
- For **maximum**:
  - Replace the **first digit** that is not `'9'` with `'9'`.
- For **minimum**:
  - If the first digit is not `'1'`, replace it with `'1'`.
  - Else, replace the first digit after that which is neither `'0'` nor `'1'` with `'0'`.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## ✅ Example

```python
Input: num = 9288

Max: Replace '2' → '9' → 9988  
Min: Replace '9' → '1' → 1288  

Output: 9988 - 1288 = 8700
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
