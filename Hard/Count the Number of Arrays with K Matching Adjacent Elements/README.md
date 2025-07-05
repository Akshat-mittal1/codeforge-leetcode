# 🔍 LeetCode [Custom] – Count Good Arrays

| Item            | Value                                                                                  |
|-----------------|----------------------------------------------------------------------------------------|
| **Solved on**   | 17‑JUNE‑2025                                                                           |
| **Category**    | Hard                                                                                   |
| **Topic Tags**  | Combinatorics, Modular Arithmetic, Exponentiation                                     |
| **Problem Link**| _Custom problem – no public link available_                                           |

---

## 📄 Problem Statement

You are given three integers: `n`, `m`, and `k`.

You need to count how many arrays of length `n` can be formed using numbers from `1` to `m` such that **exactly `k` positions** (excluding the first index) have values strictly greater than their previous index.

Return the count modulo **10^9 + 7**.

---

## 🧠 Approach

1. You choose `k` positions out of `n-1` where increases occur → **C(n - 1, k)**
2. The first element can be any number from `1` to `m` → **m**
3. For each increasing step, the next number must be greater than the previous, so choices = `m - 1`  
   → `bigpow(m - 1, n - k - 1)`

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(N) preprocessing, O(1) per query  
- **Space Complexity:** O(N) for factorial arrays

---

## ✅ Example

```python
Input:
n = 5
m = 3
k = 2

Steps:
- C(4, 2) = 6
- m = 3
- (m - 1)^(n - k - 1) = 2^2 = 4

Result: 6 * 3 * 4 = 72

Output: 72
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
