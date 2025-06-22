```markdown
# 🔍 Maximum Difference Between Increasing Elements

- 📅 Date: 16-JUNE-2025  
- 🔗 [LeetCode Link](https://leetcode.com/problems/maximum-difference-between-increasing-elements/)  
- 🧠 Category: Array, Greedy

---

## 🧾 Problem Statement

You are given a 0-indexed integer array `nums` of size `n`. The **maximum difference** between two elements `nums[i]` and `nums[j]` is defined as:

> `nums[i] - nums[j]` where `i > j` and `nums[i] > nums[j]`.

Return the maximum such difference. If no such pair exists, return -1.

---

## ✅ Approach

- Iterate through the array while tracking the minimum element encountered so far.
- For each element, calculate the difference with the current minimum.
- Update the maximum difference only if `nums[i] > premin`.

---

## 🔢 Formula

```
premin = nums[0]
for i in range(1, len(nums)):
    if nums[i] > premin:
        max_diff = max(max_diff, nums[i] - premin)
    else:
        premin = nums[i]
```

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## 🧪 Example

**Input:**  
nums = [7, 1, 5, 4]  

**Output:**  
4  
(5 - 1 = 4)

---

**👨‍💻 Author:** Akshat Mittal
```
