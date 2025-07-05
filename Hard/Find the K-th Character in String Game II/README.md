# 🔍 LeetCode 2866 – K-th Character in String Game II

| Item            | Value                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------|
| **Solved on**   | 03‑JULY‑2025                                                                                       |
| **Category**    | Medium                                                                                             |
| **Topic Tags**  | Bitmasking, Simulation                                                                             |
| **Problem Link**| [K-th Character in String Game II](https://leetcode.com/problems/k-th-character-in-string-game-ii/) |

---

## 📄 Problem Statement

Alice starts with the string `"a"`.  
She performs a series of operations on it, where each operation is either:

- `0`: Append the same string to itself.
- `1`: Append a version where each character is shifted to the next in the alphabet.

You are given an array `operations` and a large number `k`.  
You must return the **k-th character** in the final string **without actually building it**.

---

## 🧠 Approach

- Each operation **doubles** the string length.
- We simulate operations **in reverse**:
  - If `k` is in the **second half**, adjust `k -= length // 2`
  - For `op == 1`, increase shift count.
- Finally, apply the total shift to `'a'`.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---

## ✅ Example

```python
Input:
operations = [0, 1]
k = 4

Steps:
- Step 0: "a"
- Step 1: "aa"      (op 0)
- Step 2: "aabb"    (op 1)
- k = 4 → 'b'

Output: 'b'
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
