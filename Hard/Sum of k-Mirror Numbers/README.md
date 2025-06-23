# 🔍 K-Mirror Numbers

**LeetCode Link:** [K-Mirror Numbers](https://leetcode.com/problems/k-mirror-numbers/)  
**Date:** 23-JUNE-2025 
**Author:** Akshat Mittal  

---

## 📘 Problem Statement

A **k-mirror number** is a positive integer that is:
- A palindrome in base-10
- A palindrome in base-`k`

Given an integer `k` and `n`, return the **sum of the first `n` k-mirror numbers**.

---

## 💡 Approach

- Use half-number reflection to generate base-10 palindromes.
- Check each number's base-`k` representation.
- If both are palindromes, include it in the sum.
- First odd-length palindromes are generated, then even-length.

---

## 🧪 Example

**Input:**  
`k = 2`, `n = 5`

**Step-by-step:**

| Decimal | Base-10 Palindrome | Base-2  | Base-2 Palindrome |
|---------|---------------------|---------|--------------------|
| 1       | ✅                  | `1`     | ✅                 |
| 3       | ✅                  | `11`    | ✅                 |
| 5       | ✅                  | `101`   | ✅                 |
| 7       | ✅                  | `111`   | ✅                 |
| 9       | ✅                  | `1001`  | ✅                 |

**Result:**  
`1 + 3 + 5 + 7 + 9 = 25`

✅ Output: `25`

---

## 🧠 Time & Space Complexity

- **Time:** Efficient due to palindrome generation — no string slicing.
- **Space:** O(logN) — for storing digits during base conversion.

---

## 📦 Tags

`Math` `Palindrome` `Base Conversion` `Efficient Generation` `Mirror Numbers`
