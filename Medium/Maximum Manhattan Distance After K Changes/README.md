# 🔍 Leetcode 3443: Maximum Manhattan Distance After K Changes
## 📅 Date: 20-JUNE-2025  
🔗 [Leetcode Problem Link](https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/)  
🧠 **Category**: Greedy, Grid Simulation  

---

## 📄 Problem Statement

You are at origin `(0, 0)` and given a string `s` of directions (`N`, `S`, `E`, `W`).  
Each direction moves 1 step in an infinite grid.  
You're allowed to change **at most `k` directions** to any other direction.  
You must **follow the order of the string**.  
Find the **maximum Manhattan Distance** from the origin **at any time** while moving.

---

## 🧠 Approach: Greedy + Direction Counters

We count the number of times we go `N`, `S`, `E`, `W`.  
At each step, we calculate:

- ✅ `MD = |N - S| + |E - W|` = current net distance
- ✅ `i + 1` = total steps taken so far
- ✅ Boost we can get = `min(2 * k, i + 1 - MD)`

So final distance at each step =  
```text
dis = MD + min(2 * k, i + 1 - MD)
