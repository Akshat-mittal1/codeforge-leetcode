```markdown
# 🔍 Problem: Count Good Arrays

📅 Date: 2025-06-24  
🔗 Link: *(insert platform link if available)*  
🗂️ Category: Combinatorics, Modular Arithmetic, Exponentiation

---

## 📝 Problem Statement

You are given three integers: `n`, `m`, and `k`.

You need to count how many arrays of length `n` can be formed using numbers from `1` to `m` such that **exactly `k` positions** (excluding the first index) have values strictly greater than their previous index.

Return the count modulo **10^9 + 7**.

---

## ✅ Approach

1. You choose `k` positions out of `n-1` where increases occur → **C(n - 1, k)**
2. The first element can be any number from `1` to `m` → **m**
3. For each increasing step, the next number must be greater than the previous, so choices = `m - 1`
   → `bigpow(m - 1, n - k - 1)`

---

## 🔢 Formula

```
C(n - 1, k) * m * (m - 1)^(n - k - 1) % MOD
```

- `C(n, k)` is computed using precomputed factorials and modular inverse

---

## ⏱️ Time and Space Complexity

- **Time**: O(N) preprocessing, O(1) per query
- **Space**: O(N) for factorial arrays

---

## 🧪 Example

### Input:
```python
n = 5
m = 3
k = 2
```

### Output:
```python
72
```

---

## 👨‍💻 Author

Akshat Mittal
```
