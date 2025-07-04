```markdown
# 🔍 Divide String Into Groups of Size K

- 📅 Date: 22-JUNE-2025
- 🔗 [LeetCode Link](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/)  
- 🧠 Category: String, Greedy, Simulation

---

## 🧾 Problem Statement

Given a string `s`, divide it into groups of size `k`. The last group may be shorter than `k` characters. If so, fill it with the given `fill` character until its length is `k`.

Return a list of string groups.

---

## ✅ Approach

- Calculate how many characters are needed to make `s`'s length a multiple of `k`.
- Traverse `s` in steps of `k` and collect substrings.
- For the last group, if it's shorter, fill it with the `fill` character.

---

## 🔢 Formula


padding = k - (len(s) % k)
if padding != k:
    add last group with fill * padding


---

## ⏱️ Time & Space Complexity

- **Time:** O(n)
- **Space:** O(n)

---

## 🧪 Example

**Input:**  
s = "abcdefghi", k = 3, fill = "x"  

**Output:**  
["abc", "def", "ghi"]

---

**👨‍💻 Author:** Akshat Mittal
```
