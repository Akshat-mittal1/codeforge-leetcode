from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        freq_vals = sorted(freq.values())
        n = len(freq_vals)
        res = float('inf')

        for i in range(n):
            deletions = 0
            min_freq = freq_vals[i]

            # Delete all characters with freq less than min_freq
            deletions += sum(freq_vals[j] for j in range(i))

            # Delete excess characters beyond (min_freq + k)
            for j in range(i, n):
                if freq_vals[j] > min_freq + k:
                    deletions += freq_vals[j] - (min_freq + k)

            res = min(res, deletions)

        return res


# 🚀 Example
if __name__ == "__main__":
    word = "aabbcccc"
    k = 1
    sol = Solution()
    print(sol.minimumDeletions(word, k))  # Output: 1
