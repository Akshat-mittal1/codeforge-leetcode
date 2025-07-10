# 🔍 LeetCode 242 – Valid Anagram

| Item | Value |
|------|-------|
| **Solved on** | 08‑JULY‑2025 |
| **Category** | Easy |
| **Topic Tags** | Hash Table, Sorting, String |
| **Problem Link** | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) |

---

## 📄 Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

---

## 🧠 Approach

- First, check if the lengths of both strings are equal.
- If not, they can't be anagrams.
- Sort both strings and compare them character-by-character.
- If all characters match in order, the strings are anagrams.

---

## ⏱️ Time & Space Complexity

- **Time Complexity**: O(n log n) due to sorting
- **Space Complexity**: O(n) to store sorted strings

---

## ✅ Example

```python
Input: s = "anagram", t = "nagaram"
Sorted: "aaagmnr" == "aaagmnr"
Output: True

Input: s = "rat", t = "car"
Sorted: "art" != "acr"
Output: False
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
