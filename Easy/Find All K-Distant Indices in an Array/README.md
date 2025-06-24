```markdown
# 🔍 Problem: Find All K-Distant Indices in an Array
📅 Date: 2025-06-24  
🔗 Link: [LeetCode Problem](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/)  
🗂️ Category: Array, Two Pointers

---

## 📝 Problem Statement
Given an array `nums`, an integer `key`, and an integer `k`, return a list of all indices `i` such that there exists at least one index `j` where `nums[j] == key` and `abs(i - j) <= k`.

---

## ✅ Approach
1. Traverse `nums` and store all indices where the value is equal to `key`.
2. For every index `i` in the array:
   - Check if `abs(i - j) <= k` for any `j` in the key indices.
   - If true, add `i` to the result.
3. Sort and return the result.

---

## 🔢 Formula
`|i - j| <= k` where `nums[j] == key`

---

## ⏱️ Time & Space Complexity
- **Time Complexity**: `O(n * m)`  
  (where `n` is the length of `nums`, and `m` is the number of `key` occurrences)
- **Space Complexity**: `O(n)` for the result list

---

## 🧪 Example

### Input:
```python
nums = [1, 2, 3, 4, 2, 1, 2]
key = 2
k = 1
```

### Output:
```python
[0, 1, 2, 3, 4, 5, 6]
```

---

## 👨‍💻 Author
Akshat Mittal
```
