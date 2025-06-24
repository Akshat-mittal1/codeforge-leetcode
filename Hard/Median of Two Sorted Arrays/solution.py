# 🔍 Problem: Median of Two Sorted Arrays
# 📅 Date: 24-JUNE-2025
# 🔗 Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
# ✅ Approach: Merge + Sort
# ⏱️ Time Complexity: O((m+n) log(m+n)) due to sort
# 📦 Space Complexity: O(m+n) for merged array
# 🧪 Test Case:
# Input: nums1 = [1, 3], nums2 = [2]
# Merged: [1, 2, 3]
# Median: 2.0

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new = nums1 + nums2
        new.sort()
        l = len(new)
        return (new[l // 2] + new[(l // 2) - 1]) / 2.0 if l & 1 == 0 else new[l // 2]

# 🔁 Dry Run
if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    sol = Solution()
    print("Median is:", sol.findMedianSortedArrays(nums1, nums2))  # Output: 2.0
