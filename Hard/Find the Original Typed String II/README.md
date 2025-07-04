# 🔹 Possible String Count After K Repetitions

**Date:** 2025-07-03  
**Author:** Akshat Mittal  
**Category:** Dynamic Programming, Bitmasking, Combinatorics

---

## 🧩 Problem Statement

Given a string `word` consisting of characters,  
You are to find how many strings of length `k` can be formed by choosing one character from each **group of consecutive identical characters**, such that no group contributes more than its original count.

---

## 🧠 Approach

1. **Group same characters** together using run-length encoding.
2. **Count all combinations**: multiply group sizes.
3. If `k` is small (≤ number of groups), all combos are valid.
4. If `k > number of groups`, use **Dynamic Programming** to count the number of **invalid strings** of length `< k`.
5. Final Answer = total combos - invalid combos.

---

## 🔧 Formula

**Valid Strings** =  
`(total_combinations - invalid_combinations + MOD) % MOD`

---

## ⏱ Time & Space Complexity

- **Time Complexity:** O(n × k), where `n = len(groups)`
- **Space Complexity:** O(k) (can be reduced from O(n×k) using rolling arrays)

---

## ✅ Example

```python
Input:
word = "aabbcc"
k = 3

Groups = [2, 2, 2] → total = 2×2×2 = 8
All strings of length 3 are valid → Answer: 8
📌 Notes
Very useful technique in subset counting + grouped constraints

Combines run-length encoding, DP, and modulo arithmetic
