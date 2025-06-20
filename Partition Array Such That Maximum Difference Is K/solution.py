# 🔍 Problem: 2294. Partition Array Such That Maximum Difference Is K
# 📅 Date Solved: 19-JUNE-2025
# 🌐 Link: https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

# 🧠 Approach: Greedy + Sorting
#     1. Sort the array.
#     2. Start a new group whenever the current element is farther than k from
#        the smallest element of the current group.
# 🕐 Time Complexity: O(n log n)   (due to sort)
# 📦 Space Complexity: O(1)        (in‑place sort)

class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()                      # 1 Sort the array
        count = 1                        # At least one group will exist
        min_val = nums[0]                # Smallest in current group

        for num in nums[1:]:
            if num - min_val > k:        # 2 Needs a new group
                count += 1
                min_val = num            # Reset min for the new group

        return count


#  Quick Test
if __name__ == "__main__":
    nums = [3, 6, 1, 2, 5]
    k = 2
    print("Groups needed:", Solution().partitionArray(nums, k))  # Expected: 2
