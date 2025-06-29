# 2311. Longest Binary Subsequence Less Than or Equal to K

**Date**: 2025-06-29  
**Link**: [Leetcode Problem](https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k)  
**Category**: Greedy, String, Bit Manipulation

---

## 🧠 Problem Statement

Given a binary string `s` and a positive integer `k`, return the **length of the longest subsequence** of `s` such that the **binary value** of the subsequence is less than or equal to `k`.

---

## 🔍 Approach

- Traverse the string from **right to left** (LSB to MSB).
- Always include `'0'` since it does not increase the value but increases the length.
- For `'1'`, include only if its value `2^power` keeps total value ≤ `k`.
- Maintain `val` for current binary value and `power` for current bit index.

---

## 🧮 Formula

If s[i] == '0' → Always count it
If s[i] == '1' → Add if val + 2^power <= k

yaml
Copy
Edit

---

## ⏱ Time & Space Complexity

| Metric           | Complexity |
|------------------|------------|
| Time Complexity  | O(n)       |
| Space Complexity | O(1)       |

---

## 🔍 Example

**Input**:  
`s = "1001010", k = 5`  
**Output**: `5`

**Explanation**:  
Possible subsequence: `"00010"` → binary value = `2` ≤ 5 ⇒ length = 5

---

## 👨‍💻 Author

**Akshat Mittal**
