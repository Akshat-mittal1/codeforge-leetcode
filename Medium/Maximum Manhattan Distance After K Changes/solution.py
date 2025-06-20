# 🔍 Problem: 3443. Maximum Manhattan Distance After K Changes
# 📅 Date: 20-JUNE-2025
# 🌐 Link: https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/
# 🧠 Approach: Greedy with direction counters + formula (MD + min(2*k, steps - MD))
# 🕐 Time Complexity: O(n)
# 📦 Space Complexity: O(1)

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        north = south = east = west = 0
        
        for i in range(len(s)):
            c = s[i]
            if c == 'N':
                north += 1
            elif c == 'S':
                south += 1
            elif c == 'E':
                east += 1
            elif c == 'W':
                west += 1
            
            x = abs(north - south)
            y = abs(east - west)
            MD = x + y  # Current Manhattan Distance
            dis = MD + min(2 * k, i + 1 - MD)  # Max boost from remaining steps & k
            ans = max(ans, dis)
        
        return ans


# 🚀 Example Test Case
if __name__ == "__main__":
    s = "NWSE"
    k = 1
    sol = Solution()
    result = sol.maxDistance(s, k)
    print("Maximum Manhattan Distance:", result)  # Expected Output: 3
