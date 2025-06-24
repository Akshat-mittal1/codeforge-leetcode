# 🔁 Reverse Integer

- 📅 Date: 24-JUNE-2025  
- 🔗 [Leetcode Problem Link](https://leetcode.com/problems/reverse-integer/)  
- 🗂️ Category: Math, Integer Manipulation
  
---

### 📘 Problem Statement:

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2³¹, 2³¹ - 1]`, return `0`.

---

### 💡 Approach:

- Take absolute value of `x` and reverse it digit by digit.
- Multiply the result (`s`) by 10 and add last digit of `temp`.
- Continue until `temp` becomes 0.
- If reversed value exceeds 32-bit signed int range, return `0`.
- If input was negative, return `-s`, else return `s`.

---

### 🧮 Formula:

```python
s = 0
while temp > 0:
    s = s * 10 + (temp % 10)
    temp = temp // 10
⏱️ Time & Space Complexity:
Type	Complexity
🕒 Time	O(log₁₀N)
💾 Space	O(1)

🧪 Example:
python
Copy
Edit
Input: x = -123
Step-by-step:
    abs(-123) = 123
    Reverse: 321
    Negative: -321
Output: -321
python
Copy
Edit
Input: x = 120
Reverse: 21 (leading zero dropped)
Output: 21
