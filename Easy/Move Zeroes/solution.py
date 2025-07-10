class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Modifies nums in-place.
        """
        change = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != change:
                    nums[i], nums[change] = nums[change], nums[i]
                change += 1

if __name__ == "__main__":
    # ✅ Test Case 1
    nums1 = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums1)
    print(nums1)  # Output: [1, 3, 12, 0, 0]

    # ✅ Test Case 2
    nums2 = [0, 0, 1]
    Solution().moveZeroes(nums2)
    print(nums2)  # Output: [1, 0, 0]
