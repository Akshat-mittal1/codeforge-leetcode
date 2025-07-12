# 🔍 LeetCode 3445 – Maximum Difference Between Even and Odd Frequency II

| Item            | Value                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------------|
| **Solved on**   | 11‑JUNE‑2025                                                                                                 |
| **Category**    | Medium                                                                                                       |
| **Topic Tags**  | Sliding Window, Prefix Sum, Digit Frequency                                                                  |
| **Problem Link**| [Maximum Difference Between Even and Odd Frequency II](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/) |

---

## 📄 Problem Statement

You are given a string `sequence` consisting of digits from **0 to 4**, and an integer `window_size`.  
Your task is to find the **maximum possible value of**:

count(a) - count(b)

Where:
- `a ≠ b`
- Both digits must appear **at least once** in the window of size `window_size`.

---

## 🧠 Approach

1. Iterate over all 25 digit pairs `(a, b)` where `a ≠ b`.
2. For each pair:
   - Use a sliding window of length `window_size`.
   - Use prefix sums and parity optimization to track the frequency difference of the two digits.
   - Map parities using: `((x % 2) << 1) | (y % 2)` to minimize storage.
3. Track maximum difference only when both digits are present in the window.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(25 × n)  
- **Space Complexity:** O(n)

---

## ✅ Example

```python
Input:
sequence = "120201201"
window_size = 5

Possible Window: "20120"
→ count(2) = 2, count(0) = 1 → diff = 1
→ count(1) = 1, count(2) = 2 → diff = 1

Output: 2
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
