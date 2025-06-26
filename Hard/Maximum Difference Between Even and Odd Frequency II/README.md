# Maximum Difference Between Counts of Two Digits in a Sliding Window

**Date:** 11-JUNE-2025
**Category:** Sliding Window, Prefix Sum, Digit Frequency

---

### 🧠 Problem Statement:
You are given a string `sequence` consisting of digits from **0 to 4**, and an integer `window_size`.  
Your task is to find the **maximum possible value of**:

count(a) - count(b)

yaml
Copy
Edit

where `a ≠ b`, and both digits appear at least once in the window of size `window_size`.

---

### 💡 Approach:

1. For every possible pair of digits `(a, b)` where `a ≠ b`:
   - Traverse the string using a **sliding window**.
   - Track the cumulative counts of both digits using a **prefix sum array**.
   - Use a **custom `get(x, y)` function** to handle parity and optimize `min_diff` tracking.
2. Update the result only when both `a` and `b` have been encountered within the window.

---

### ⚙️ Core Logic:
- Uses `((x % 2) << 1) | (y % 2)` to map count parities into 4 categories for efficient lookup.
- Maintains a `min_diff` array of size 4 to minimize space and maximize reuse.

---

### 🧪 Test Case:

```python
Input:
    sequence = "120201201"
    window_size = 5

Output:
    (Expected output varies — example: 2 or 3 depending on digit frequencies)
⏱️ Time & Space Complexity:
Metric	Value
Time	O(25 × n)
Space	O(n)
Explanation	25 digit pairs (0–4), each full pass over sequence

📌 Notes:
Skips pairs where a == b or if either digit doesn’t appear.

Efficient for long sequences due to bounded digit range and parity-based optimization.
