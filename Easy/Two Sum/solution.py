class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = {}  # Dictionary to store number and its index

        for i, item in enumerate(nums):
            find = target - item
            if find in n:
                return [n[find], i]
            n[item] = i  # Store the index of the current number


if __name__ == "__main__":
    # ✅ Example usage
    sol = Solution()
    result = sol.twoSum([2, 7, 11, 15], 9)
    print("Output:", result)  # Output: [0, 1]
