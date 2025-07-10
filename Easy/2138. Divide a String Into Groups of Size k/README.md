# 🔍 LeetCode 2138 – Divide a String Into Groups of Size K

| Item            | Value                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------|
| **Solved on**   | 22‑JUNE‑2025                                                                                   |
| **Category**    | Easy                                                                                           |
| **Topic Tags**  | String, Greedy, Simulation                                                                     |
| **Problem Link**| [Divide a String Into Groups of Size K](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/) |

---

## 📄 Problem Statement

Given a string `s`, divide it into groups of size `k`. The last group may be shorter than `k` characters. If so, fill it with the given `fill` character until its length is `k`.

Return a list of string groups.

---

## 🧠 Approach

- Calculate how many characters are needed to make `s`'s length a multiple of `k`.
- Traverse `s` in steps of `k` and collect substrings.
- For the last group, if it's shorter, fill it with the `fill` character.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

---

## ✅ Example

```python
Input:
s = "abcdefghi", k = 3, fill = "x"

Steps:
- Groups: "abc", "def", "ghi"
- No padding needed

Output: ["abc", "def", "ghi"]
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
