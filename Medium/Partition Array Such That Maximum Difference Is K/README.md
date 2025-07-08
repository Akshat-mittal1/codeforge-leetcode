# 🔍 LeetCode 2294 – Partition Array Such That Maximum Difference Is K

| Item            | Value                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------|
| **Solved on**   | 19‑06‑2025                                                                                            |
| **Category**    | Medium                                                                                                |
| **Topic Tags**  | Greedy, Sorting                                                                                       |
| **Problem Link**| [Partition Array Such That Maximum Difference Is K](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/) |

---

## 📄 Problem Statement

Given an integer array `nums` and an integer `k`,  
split `nums` into the **minimum number of non-empty groups**  
such that the **difference between the maximum and minimum** element in each group is **at most `k`**.

Return the **minimum number of groups** needed.

---

## 🧠 Approach (Greedy + Sort)

1. **Sort** the array.
2. Start with the first element as the **min of the current group**.
3. Traverse the array:
   - If `num - min_val > k`, start a **new group**.
   - Else, continue in the current group.
4. Increment group count every time a new group starts.

### ✅ Why it works:
- After sorting, all close numbers are adjacent.
- Once `num - min_val > k`, no future number can join the current group — so we **greedily start a new one**.

---

## ⏱️ Time & Space Complexity

| Type              | Value        |
|-------------------|--------------|
| Time Complexity   | O(n log n)   |
| Space Complexity  | O(1)         |

---

## ✅ Example

```python
Input: nums = [3, 6, 1, 2, 5], k = 2
Sorted: [1, 2, 3, 5, 6]

Group 1: [1, 2, 3] → max - min = 2
Group 2: [5, 6] → max - min = 1

Output: 2
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
