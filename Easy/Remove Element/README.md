# 🔍 LeetCode 27 – Remove Element

| Item            | Value                                                   |
|-----------------|---------------------------------------------------------|
| **Solved on**   | 12‑JUNE‑2025                                            |
| **Category**    | Easy                                                    |
| **Topic Tags**  | Array, Two Pointers                                     |
| **Problem Link**| [Remove Element](https://leetcode.com/problems/remove-element/) |

---

## 📄 Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` **in-place**.  
Return the number of elements after removal. The elements in the first `k` positions should be valid (order can change).  
**Note**: Do not use extra space. Modify `nums` in-place.

---

## 🧠 Approach (Used in Code)

- Count how many times the value `val` appears using `nums.count(val)`.
- Use a loop to repeatedly remove `val` using `remove()`.
- Then, for visualization (not required by the original problem), append underscores `_` to fill up removed spaces.
- Return the new length `k = total_length - count(val)`.

> ⚠️ Note: This approach is **not optimal** because `list.remove(val)` is O(n), making the whole logic O(n²).  
> A better approach is the **two-pointer** method (see below in bonus).

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n²) due to repeated `remove()` calls  
- **Space Complexity:** O(1) — in-place modification, no extra storage used

---

## ✅ Example

```python
Input: nums = [3, 2, 2, 3], val = 3
Process:
- Count of 3's = 2
- Remove all 3's → [2, 2]
- Append '_' to keep list length → [2, 2, '_', '_']
Output:
- New length: 2
- Modified nums: [2, 2, '_', '_']
```

## ---

👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
