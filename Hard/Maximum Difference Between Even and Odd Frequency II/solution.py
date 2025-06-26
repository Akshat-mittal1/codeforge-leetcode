# Title: Maximum Difference Between Counts of Two Digits in a Sliding Window
# Date: 2025-06-26
# Approach: Prefix sum tracking, custom encoding of parity, sliding window optimization
# Time Complexity: O(25 * n), where 25 is for digit pairs (0–4) and n is length of sequence
# Space Complexity: O(n)
# Test Case: sequence = "120201201", window_size = 5

class Solution(object):
    def get(self, x, y):
        return ((x % 2) << 1) | (y % 2)

    def dfs(self, sequence, char_a, char_b, window_size, length):
        count_a = count_b = 0
        prefix_sum = [(0, 0)] * length
        min_diff = [float('inf')] * 4
        result = float('-inf')
        start = 0

        for i in range(length):
            char = sequence[i]
            if char == char_a:
                count_a += 1
            elif char == char_b:
                count_b += 1

            if i - window_size + 1 == 0:
                min_diff[0] = 0

            while start + window_size <= i and prefix_sum[start][0] < count_a and prefix_sum[start][1] < count_b:
                diff = prefix_sum[start][0] - prefix_sum[start][1]
                index = self.get(prefix_sum[start][0], prefix_sum[start][1])
                min_diff[index] = min(min_diff[index], diff)
                start += 1

            ri = self.get(count_a + 1, count_b)
            if min_diff[ri] != float('inf') and count_a > 0 and count_b > 0:
                result = max(result, count_a - count_b - min_diff[ri])

            prefix_sum[i] = (count_a, count_b)

        return result

    def maxDifference(self, sequence, window_size):
        """
        :type sequence: str
        :type window_size: int
        :rtype: int
        """
        length = len(sequence)
        result = float('-inf')
        count_map = [0] * 5

        for char in sequence:
            count_map[int(char)] += 1

        for a in range(5):
            for b in range(5):
                if a == b or count_map[a] == 0 or count_map[b] == 0:
                    continue

                current_result = self.dfs(sequence, str(a), str(b), window_size, length)
                result = max(result, current_result)

        return result


# ✅ Test Case
if __name__ == "__main__":
    sequence = "120201201"
    window_size = 5
    sol = Solution()
    print("Output:", sol.maxDifference(sequence, window_size))  # Example Output
