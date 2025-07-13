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
