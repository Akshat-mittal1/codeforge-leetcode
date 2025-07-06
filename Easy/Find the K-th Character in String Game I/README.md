# 🔍 LeetCode 3304 – Find the K-th Character in Concatenated String

| Item              | Value                                                                |
|-------------------|----------------------------------------------------------------------|
| **Solved on**     | 05‑JULY‑2025                                                         |
| **Category**      | Medium                                                               |
| **Topic Tags**    | Simulation, Strings                                                  |
| **Problem Link**  | [Find the K-th Character in Concatenated String](https://leetcode.com/problems/find-the-k-th-character-in-concatenated-string/) |

---

## 📄 Problem Statement

You are given an integer `k`. You must simulate the following process to find the `k`-th character of the final string:

1. Start with `word = "a"`.
2. Create a new string by converting each character in `word` to the next letter in the alphabet (wrapping `'z'` to `'a'`).
3. Append the new string to `word`.
4. Repeat steps 2–3 until the length of `word` is at least `k`.

Return the `k`-th character (1-indexed) of `word`.

---

## 🧠 Approach

- Begin with `word = "a"`.
- Repeatedly:
  - Construct `add` string by shifting every character of `word` (e.g., `'a' → 'b'`, `'z' → 'a'`).
  - Append `add` to `word`.
- Stop once `len(word) ≥ k`.
- Return `word[k - 1]`.

This process ensures that we only generate as much of the string as needed.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(k) – we construct the string until length `k`
- **Space Complexity:** O(k) – entire string is stored up to length `k`

---

## ✅ Example (with explanation)

```python
Input:
k = 5

word = "a"        # length = 1
+ "b" → "ab"      # length = 2
+ "bc" → "abbc"   # length = 4
+ "ccd" → "abbcbccd" # length = 8

word = "a b b c b c c d"
Index:  1 2 3 4 5 6 7 8

word[5] = 'b'
Output: 'b'
```

## 👨‍💻 Author: [akshat-mittal1](https://github.com/akshat-mittal1)
