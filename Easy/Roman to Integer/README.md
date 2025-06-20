# 🔍 LeetCode 13 – Roman to Integer

| Item | Value |
|------|-------|
| **Solved on** | 18‑06‑2025 |
| **Category** | Easy |
| **Topic Tags** | Strings, Hash Map, Greedy |
| **Problem Link** | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) |

---

## 📄 Problem Statement

Given a Roman numeral string `s`, convert it into its corresponding integer.

**Roman numerals rules:**

- Basic symbols:
  - `I = 1`, `V = 5`, `X = 10`, `L = 50`
  - `C = 100`, `D = 500`, `M = 1000`
- Subtractive cases:
  - `IV = 4`, `IX = 9`
  - `XL = 40`, `XC = 90`
  - `CD = 400`, `CM = 900`

---

## 🧠 Approach

- Traverse each character of the string `s`.
- For subtractive patterns (e.g., `IV`, `IX`, etc.), check if the **next symbol is larger** than current:
  - If yes, subtract current from total.
  - Else, add current's value.
- Use a loop with `enumerate` and look-ahead logic.

---

## ✅ Example

```python
Input: "MCMXCIV"
Breakdown: 
M = 1000  
CM = 900  
XC = 90  
IV = 4  

Total = 1000 + 900 + 90 + 4 = 1994
