# 🔹 K-th Character in Generated String

**Date:** 03-JULY-2025
**Category:** Bitmasking / Simulation  
**Author:** Akshat Mittal

---

## 🧩 Problem Statement

Alice starts with the string `"a"`.  
She performs a series of operations on it, where each operation is either:

- `0`: Append the same string to itself.
- `1`: Append a version where each character is shifted to the next in the alphabet.

You are given an array `operations` and a large number `k`.  
You must return the **k-th character** in the final string without actually building it.

---

## ✅ Approach

- Each operation **doubles** the string.
- We simulate the reverse:
  - Check whether the `k-th` character was from the first or second half.
  - If from the second half:
    - For `op == 1`, count how many times shift should happen.
- Finally, apply the shift to `'a'`.

---

## 🔍 Formula

Final character =  
`chr((ord('a') + shift_count) % 26 + ord('a'))`

Where `shift_count` = number of `1` operations that affected k-th position.

---

## ⏱ Time & Space

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n) due to list storing shift operations

---

## 🧪 Example

```python
operations = [0, 1]
k = 4

# Explanation:
# Step 0: "a"
# Step 1: "aa"      (op 0)
# Step 2: "aabb"    (op 1)
# k = 4 → 'b'

Output: 'b'

