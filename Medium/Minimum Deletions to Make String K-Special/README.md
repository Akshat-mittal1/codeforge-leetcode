# 🔍 Custom Problem: Make String K-Special (Minimum Deletions)
## 📅 Date: 21-JUNE-2025  
🔗 (Custom problem – no official link)  
🧠 **Category**: Greedy, Frequency Analysis  

---

## 📄 Problem Statement

You're given a string `word` and an integer `k`.  
A string is called **k-special** if for all characters `i` and `j`,  
```
|freq(i) - freq(j)| <= k
```

Return the **minimum number of deletions** required to make the string k-special.

---

## 🧠 Approach: Greedy + Sorted Frequencies

1. Count frequency of each character.
2. Sort the frequencies.
3. Try every frequency as the **minimum allowed** frequency:
   - Delete all characters with lower frequency.
   - Reduce characters with too high frequency to fit in range `[min_freq, min_freq + k]`.
4. Return the minimum deletions across all valid configurations.

---

### Formula:
```
deletions = sum(freqs < min_freq) + sum(extra in freqs > min_freq + k)
```

---

## ✅ Time & Space

- ⏱ Time Complexity: O(n²)
- 💾 Space Complexity: O(n)

---

## 🧪 Example

```python
Input: word = "aabbcccc", k = 1
Output: 1
```

---

## 🧑‍💻 Author

Leetcode-style implementation by Akshat Mittal  
Includes clean greedy logic using frequency band control
