# 🔹 Problem Title: Possible String Count After K Repetitions
# 🔹 Approach: Grouping + DP + Modulo Arithmetic
# 🔹 Date: 02-JULY-20252
# 🔹 Time Complexity: O(n * k), where n = len(groups)
# 🔹 Space Complexity: O(k)
# 🔹 Author: Akshat Mittal

class Solution:
    MOD = 10**9 + 7

    def possibleStringCount(self, word, k):
        if not word:
            return 0

        # Step 1: Group same characters
        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        # Step 2: Calculate total combinations without length restriction
        total = 1
        for g in groups:
            total = (total * g) % self.MOD

        # Step 3: If k is small, all combos are valid
        if k <= len(groups):
            return total

        # Step 4: DP to count "invalid" strings (length < k)
        dp = [0] * k
        dp[0] = 1  # base case

        for g in groups:
            new_dp = [0] * k
            sum_val = 0
            for s in range(k):
                if s > 0:
                    sum_val = (sum_val + dp[s - 1]) % self.MOD
                if s > g:
                    sum_val = (sum_val - dp[s - g - 1] + self.MOD) % self.MOD
                new_dp[s] = sum_val
            dp = new_dp

        # Step 5: Final valid strings = total - invalid (with len < k)
        invalid = sum(dp[len(groups):k]) % self.MOD
        return (total - invalid + self.MOD) % self.MOD


# 🔍 Test Cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("aabbcc", 3),   # Expected: 8
        ("aabbcc", 4),   # Expected: 7
        ("aaaa", 2),     # Expected: 3
        ("abc", 2),      # Expected: 1
        ("abcabc", 5),   # Expected: 1
    ]

    for word, k in test_cases:
        print(f"word = '{word}', k = {k} → {sol.possibleStringCount(word, k)}")

