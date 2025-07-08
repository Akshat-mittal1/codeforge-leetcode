# 🔍 LeetCode 2294 – Partition Array Such That Maximum Difference Is K

| Item | Value |
|------|-------|
| **Solved on** | 19‑06‑2025 |
| **Category** | Greedy / Sorting |
| **Difficulty** | Medium |
| **Link** | <https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/> |

---

## 📝 Problem Statement (abridged)

Given an integer array `nums` and an integer `k`, split `nums` into the minimum number<br>
of non‑empty **groups** such that the **difference between the maximum and minimum element** in each group is **≤ k**.  
Return that minimum number of groups.

---

## 🧠 Approach

1. **Sort** `nums` (ascending).  
2. **Greedy sweep**:  
   - Keep track of the **smallest element** of the current group (`min_val`).  
   - For every next element `num`:  
     - If `num − min_val > k`, start a **new group** (`count += 1`) and reset `min_val = num`.  
     - Else, keep the element in the current group.  
3. The variable `count` is the answer.

### Why it works

Sorting places close numbers together. Once an element is more than `k` away from the group's minimum, **no later element (>= num)** can fit in that group either, so greedily starting a new group is optimal.

---

## ⏱️ Complexity

| Type | Complexity |
|------|------------|
| **Time** | `O(n log n)` (sorting) |
| **Space** | `O(1)` (in‑place sort) |

---

## 💡 Example

```text
nums = [3, 6, 1, 2, 5], k = 2
Sorted → [1, 2, 3, 5, 6]

Group 1: [1, 2, 3]   (max − min = 3 − 1 = 2 ≤ k)
Group 2: [5, 6]      (6 − 5 = 1 ≤ k)

Answer = 2 groups
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)

