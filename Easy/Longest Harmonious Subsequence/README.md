```markdown
# Longest Harmonious Subsequence
**Date**: 2025-06-30  
**Link**: [LeetCode Problem](https://leetcode.com/problems/longest-harmonious-subsequence/)  
**Category**: Array, HashMap, Two Pointers

---

### 🧠 Problem Statement
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.  
Given an integer array `nums`, return the length of the longest harmonious subsequence among all its possible subsequences.

---

### 🚀 Approach
- Sort the array
- Use two pointers (`j` and `i`) to find the longest window where `nums[i] - nums[j] == 1`
- Update max length accordingly

---

### ⏱️ Time and Space Complexity
- **Time**: O(n log n) — due to sorting
- **Space**: O(1) — no extra memory used

---

### 💡 Example
**Input**: `[1, 3, 2, 2, 5, 2, 3, 7]`  
**Output**: `5`  
**Explanation**: The subsequence `[3, 2, 2, 2, 3]` is valid.

---

### 🧪 Test Run
```python
test_input = [1, 3, 2, 2, 5, 2, 3, 7]
print(Solution().findLHS(test_input))  # Output: 5
```

---

### 👨‍💻 Author
Akshat Mittal
```

