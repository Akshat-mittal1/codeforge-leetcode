# 🔍 LeetCode 2597 – Count the Number of Arrays with K Matching Adjacent Elements

| Item            | Value                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| **Solved on**   | 17‑JUNE‑2025                                                                                              |
| **Category**    | Hard                                                                                                      |
| **Topic Tags**  | Combinatorics, Modular Arithmetic, Exponentiation                                                        |
| **Problem Link**| [Count the Number of Arrays with K Matching Adjacent Elements](https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements) |

---

## 📄 Problem Statement

You are given three integers: `n`, `m`, and `k`.

You need to count how many arrays of length `n` can be formed using numbers from `1` to `m` such that **exactly `k` positions** (excluding the first index) have values **equal to** their previous index.

Return the count modulo **10^9 + 7**.

---

## 🧠 Approach

1. You choose `k` positions out of `n-1` where adjacent values will match → **C(n - 1, k)**
2. The first element can be any number from `1` to `m` → **m**
3. For the remaining `n - k - 1` positions (which must differ from the previous), we have `(m - 1)` choices per position.  
   → Use fast exponentiation: `(m - 1)^(n - k - 1)`

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(N) preprocessing, O(1) per query  
- **Space Complexity:** O(N) for factorials and inverses

---

## ✅ Example

```python
Input:
n = 5
m = 3
k = 2

Steps:
- Choose 2 positions where adjacent elements are equal: C(4, 2) = 6
- First element has m = 3 choices
- The other (n - k - 1) = 2 positions must differ from previous → (m - 1)^2 = 2^2 = 4

Result: 6 * 3 * 4 = 72

Output: 72

```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
