# Maximum Difference by Remapping a Digit

**Date**: 14-JUNE-2025
**Link**: [LeetCode - Maximum Difference by Remapping a Digit](https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/)  
**Category**: Greedy, Math, String

---

## 🧩 Problem Statement

You are given an integer `num`. You must choose a digit and **replace all occurrences** of it in the number with **another digit** (0–9) such that:

- After one transformation (to get max),
- And another transformation (to get min),

Return the **difference** between max and min you can get.

---

## 🚀 Approach

1. Convert the number to a string.
2. For maximum:
   - Replace the first non-9 digit with 9.
3. For minimum:
   - Replace the first digit with 0.
4. Reconstruct both numbers digit by digit.
5. Return `max - min`.

---

## ⏱️ Time & Space Complexity

- **Time**: O(d), where `d = number of digits in num`
- **Space**: O(1)

---

## 💡 Example

```python
Input: num = 11891
Max version: 99899
Min version: 11001
Output: 99899 - 11001 = 88898

