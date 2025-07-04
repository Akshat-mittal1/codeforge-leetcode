# Count Possible Strings Without Changing Order
**Date**: 01-JULY-2025
**Link**: (Your problem link or custom URL)  
**Category**: String Processing

---

### Problem Statement:
You are given a string. Count how many positions in the string have a character equal to the previous one. This represents possible positions where you could make a substitution or mark repetition, preserving the order.

---

### Approach:
- Start with a counter `a = 1` (the original string is always valid).
- Iterate from the second character to the end.
- If current character is same as previous, increment the counter.
- Return the final count.

---

### Formula:
If `word[i] == word[i-1]`, then `count += 1`.

---

### Time & Space Complexity:
- **Time**: O(n), where n is the length of the string
- **Space**: O(1), no extra space used

---

### Example:
```python
Input: "aabbcc"
Output: 3
Explanation: 'aa', 'bb', and 'cc' have repetitions.
```
```
Author: Akshat Mittal
```
