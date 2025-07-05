from bisect import bisect_right, bisect_left

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def count_less_equal(x):
            count = 0
            for a in nums1:
                if a > 0:
                    count += bisect_right(nums2, x // a)
                elif a < 0:
                    count += len(nums2) - bisect_left(nums2, (x + (-1 if x % a else 0)) // a)
                else:
                    if x >= 0:
                        count += len(nums2)
            return count

        left, right = -10**10, 10**10
        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left


# ✅ Test Case
if __name__ == "__main__":
    nums1 = [-4, -2, 0, 3]
    nums2 = [1, 2]
    k = 6

    sol = Solution()
    result = sol.kthSmallestProduct(nums1, nums2, k)
    print("Output:", result)  # Expected: 0
# Title: K-th Smallest Product of Two Sorted Arrays
# Date: 25-JUNE-2025
# Link: https://leetcode.com/problems/k-th-smallest-product-of-two-sorted-arrays/
# Approach: Binary Search on Answer
# Time Complexity: O((m + n) * log(range))
# Space Complexity: O(1)
# Test Case: nums1 = [-4, -2, 0, 3], nums2 = [1, 2], k = 6

from bisect import bisect_right, bisect_left

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def count_less_equal(x):
            count = 0
            for a in nums1:
                if a > 0:
                    count += bisect_right(nums2, x // a)
                elif a < 0:
                    count += len(nums2) - bisect_left(nums2, (x + (-1 if x % a else 0)) // a)
                else:
                    if x >= 0:
                        count += len(nums2)
            return count

        left, right = -10**10, 10**10
        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
