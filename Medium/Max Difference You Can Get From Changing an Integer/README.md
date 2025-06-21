# 🔍 Leetcode 1432: Max Difference You Can Get From Changing an Integer
## 📅 Date: 15-JUNE-2025  
🔗 [Leetcode Problem Link](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/)  
🧠 **Category**: Greedy, String Manipulation  

---

## 📄 Problem Statement

You are given an integer `num`. You can choose two digits (not necessarily distinct) and replace **all occurrences** of the first digit in `num` with the second digit.

- You must do this for **two separate replacements**:
  - One to get the **maximum** number possible
  - One to get the **minimum** number possible

Return the **difference between max and min** you can achieve after both operations.

---

## 🧠 Approach: Greedy Replacement

- Convert the number to string.
- For max:
  - Replace the **first non-9 digit** with '9'.
- For min:
  - If first digit ≠ '1', replace it with '1'.
  - Else, replace the first non-[0,1] digit after it with '0'.

---

### Formula:
```
result = max_possible - min_possible
```

---

## ✅ Time & Space

- ⏱ Time Complexity: O(n)  
- 💾 Space Complexity: O(n)

---

## 🧪 Example

```python
Input: num = 9288
Output: 8700
```

---

## 🧑‍💻 Author

Leetcode-style greedy implementation by Akshat Mittal.
