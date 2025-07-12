# 🔍 LeetCode 3443 – Maximum Manhattan Distance After K Changes

| Item            | Value                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| **Solved on**   | 20‑JUNE‑2025                                                                                               |
| **Category**    | Medium                                                                                                     |
| **Topic Tags**  | Greedy, Grid Simulation                                                                                    |
| **Problem Link**| [Maximum Manhattan Distance After K Changes](https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/) |

---

## 📄 Problem Statement

You are at origin `(0, 0)` and given a string `s` of directions (`N`, `S`, `E`, `W`).  
Each direction moves 1 step in an infinite grid.  
You're allowed to change **at most `k` directions** to any other direction.  
You must **follow the order of the string**.  
Find the **maximum Manhattan Distance** from the origin **at any time** while moving.

---

## 🧠 Approach (Greedy + Direction Counters)

- Maintain counters for each direction: `N`, `S`, `E`, `W`
- At each step:
  - Compute net vertical movement: `abs(N - S)`
  - Compute net horizontal movement: `abs(E - W)`
  - Total manhattan distance: `MD = vertical + horizontal`
  - You can gain extra distance using `k` changes:
    - Max boost: `min(2 * k, steps_so_far - MD)`
  - Final possible distance at that point: `MD + boost`
- Track the **maximum** distance across all steps.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---

## ✅ Example

```python
Input:
s = "NSEW"
k = 1

Step-by-step:
1. Move N → (0, 1) → MD = 1
2. Move S → (0, 0) → MD = 0
3. Move E → (1, 0) → MD = 1
4. Move W → (0, 0) → MD = 0

With up to 1 change, max boost = 2  
Maximum MD achieved = 0 + 2 = 2

Output: 2
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)

