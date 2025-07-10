class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = -1
        for i in range(1, len(nums)):
            x = nums[:i]
            if maximum < nums[i] - min(x) and nums[i] != min(x):
                maximum = nums[i] - min(x)
        return maximum

# 🧪 Example Test Case
if __name__ == "__main__":
    nums = [7, 1, 5, 4]
    obj = Solution()
    print(obj.maximumDifference(nums))  # Output: 4
